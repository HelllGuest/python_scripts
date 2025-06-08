#!/usr/bin/env python3
"""
List all installed Android apps via ADB, including system, user, and vendor apps.
Supports output in TXT (default), JSON, or CSV formats.

Features:
- Partition filtering (e.g., system, user, vendor)
- Custom output paths
- App metadata (label, version)
- Colored summary in console
- Quiet and verbose modes
- Graceful error handling

Usage Examples:
  python list_installed_android_apps.py --format txt --partition user system
  python list_installed_android_apps.py --no-meta --output apps.csv --format csv

Dependencies:
- Requires adb installed and accessible in system PATH.
- No external Python packages required.

Author: Anoop Kumar
Date: 2025-06-08  
"""

import argparse
import subprocess
import sys
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional

# --- Constants for formatting and config ---
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_CYAN = "\033[96m"
COLOR_YELLOW = "\033[93m"
COLOR_MAGENTA = "\033[95m"
COLOR_BLUE = "\033[94m"
COLOR_BOLD = "\033[1m"
COLOR_RED = "\033[91m"

SUPPORTED_FORMATS = ["txt", "json", "csv"]
ADB_COMMAND_PREFIX = ["adb"]

# --- ADB Helpers ---

def run_adb_command(command: str, fail_silently: bool = False) -> List[str]:
    full_command = ADB_COMMAND_PREFIX + ["shell"] + command.split()
    try:
        result = subprocess.run(
            full_command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().splitlines()
    except subprocess.CalledProcessError as e:
        if fail_silently:
            return []
        print(f"{COLOR_RED}❌ ADB command failed: {e.stderr.strip()}{COLOR_RESET}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"{COLOR_RED}❌ ADB not found. Make sure it's installed and in your PATH.{COLOR_RESET}")
        sys.exit(1)

def check_device_connected() -> None:
    try:
        result = subprocess.run(
            ADB_COMMAND_PREFIX + ["devices"],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().splitlines()
        devices = [
            line for line in lines if "\tdevice" in line and
            not any(state in line for state in ["unauthorized", "offline"])
        ]
        if not devices:
            print(f"{COLOR_RED}❌ No connected and authorized Android devices found.{COLOR_RESET}")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"{COLOR_RED}❌ ADB command failed: {e.stderr.strip()}{COLOR_RESET}")
        sys.exit(1)

# --- Metadata Parsing ---

def get_device_info() -> Dict[str, str]:
    manufacturer = run_adb_command("getprop ro.product.manufacturer", fail_silently=True)
    model = run_adb_command("getprop ro.product.model", fail_silently=True)
    version = run_adb_command("getprop ro.build.version.release", fail_silently=True)
    return {
        "manufacturer": manufacturer[0] if manufacturer else "Unknown",
        "model": model[0] if model else "Unknown",
        "android_version": version[0] if version else "Unknown"
    }

def get_app_label_and_version(package_name: str) -> Dict[str, str]:
    try:
        output = run_adb_command(f"dumpsys package {package_name}", fail_silently=True)
        label = version = "Unknown"
        for line in output:
            if "application-label:" in line:
                label = line.split("application-label:")[-1].strip().strip("'\"")
            elif "versionName=" in line:
                version = line.split("versionName=")[-1].strip()
        return {"label": label or package_name, "version": version}
    except (IndexError, ValueError):
        return {"label": package_name, "version": "Unknown"}

def parse_package_line(line: str) -> Optional[Dict[str, str]]:
    try:
        if not line.startswith("package:"):
            return None
        apk_path, package_name = line[8:].split("=", 1)
        partition_map = {
            "/system/": "system",
            "/vendor/": "vendor",
            "/product/": "product",
            "/odm/": "odm",
            "/data/": "user"
        }
        partition = "unknown"
        for prefix, name in partition_map.items():
            if apk_path.startswith(prefix):
                partition = name
                break
        return {
            "apk_path": apk_path,
            "package_name": package_name,
            "partition": partition
        }
    except ValueError:
        return None

# --- Output Generation ---

def generate_text_report(apps: List[Dict[str, str]], device_info: Dict[str, str]) -> str:
    lines = [
        f"Installed Android Apps Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Device: {device_info['manufacturer']} {device_info['model']} (Android {device_info['android_version']})",
        "=" * 70
    ]
    partitions = {}
    for app in apps:
        partitions.setdefault(app["partition"], []).append(app)

    for part, part_apps in sorted(partitions.items()):
        lines.append(f"\n{part.capitalize()} Apps ({len(part_apps)}):")
        lines.append("-" * 70)
        for app in part_apps:
            lines.extend([
                f"{'Package Name':<15}: {app['package_name']}",
                f"{'APK Path':<15}: {app['apk_path']}",
                f"{'Label':<15}: {app.get('label', 'Unknown')}",
                f"{'Version':<15}: {app.get('version', 'Unknown')}",
                "-" * 70
            ])
    return "\n".join(lines)

def write_report(apps: List[Dict[str, str]], device_info: Dict[str, str], fmt: str, path: Optional[str]) -> str:
    filename = path or f"installed_apps_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{fmt}"

    try:
        if fmt == "txt":
            with open(filename, "w", encoding="utf-8") as f:
                f.write(generate_text_report(apps, device_info))
        elif fmt == "json":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump({"device_info": device_info, "apps": apps}, f, indent=2)
        elif fmt == "csv":
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["partition", "package_name", "apk_path", "label", "version"])
                writer.writeheader()
                for app in apps:
                    writer.writerow(app)
        else:
            print(f"{COLOR_RED}❌ Unsupported format: {fmt}{COLOR_RESET}")
            sys.exit(1)
    except IOError as e:
        print(f"{COLOR_RED}❌ Error writing report to {filename}: {e}{COLOR_RESET}")
        sys.exit(1)

    return filename

def print_partition_summary(apps: List[Dict[str, str]], device_info: Dict[str, str]) -> None:
    print(f"📱 Device: {device_info['manufacturer']} {device_info['model']} (Android {device_info['android_version']})")
    print(f"📦 App Summary:")
    
    # Calculate counts for each partition
    part_counts = {}
    total_apps = 0
    for app in apps:
        part_counts.setdefault(app['partition'], 0)
        part_counts[app['partition']] += 1
        total_apps += 1

    # Sort partitions alphabetically and then add 'total' at the end
    sorted_parts = sorted(part_counts.items())
    
    # Determine max partition name length for alignment
    max_part_len = max(len(part) for part, _ in sorted_parts) if sorted_parts else 0

    color_cycle = [COLOR_CYAN, COLOR_YELLOW, COLOR_MAGENTA, COLOR_BLUE, COLOR_GREEN] # Adjusted cycle for contrast

    for i, (part, count) in enumerate(sorted_parts):
        prefix = "├─" if i < len(sorted_parts) - 1 else "└─"
        color = color_cycle[i % len(color_cycle)]
        print(f"  {prefix} {color}{part:<{max_part_len}} : {count} apps{COLOR_RESET}")
    
    # Add total line
    if sorted_parts: # Only add total if there are apps
        print(f"  └─ {COLOR_BOLD}total{COLOR_RESET}{' ' * (max_part_len - 5)} : {COLOR_BOLD}{total_apps} apps{COLOR_RESET}")


# --- Main Execution ---

def main():
    parser = argparse.ArgumentParser(description="List all installed Android apps via ADB.")
    parser.add_argument("--format", choices=SUPPORTED_FORMATS, default="txt", help="Output format.")
    parser.add_argument("--verbose", action="store_true", help="Print full report to console.")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress output.")
    parser.add_argument("--no-meta", action="store_true", help="Skip fetching label/version info (faster).")
    parser.add_argument("--partition", nargs="*", help="Filter by partition(s) (e.g., user system vendor).")
    parser.add_argument("--output", help="Specify full output file path.")
    args = parser.parse_args()

    check_device_connected()
    raw_lines = run_adb_command("pm list packages -f")
    if not raw_lines:
        print(f"{COLOR_YELLOW}⚠️ No package data returned from ADB.{COLOR_RESET}")
        sys.exit(0)

    total = len(raw_lines)
    apps = []
    for i, line in enumerate(raw_lines, 1):
        pkg = parse_package_line(line)
        if pkg:
            if args.partition and pkg["partition"] not in [p.lower() for p in args.partition]:
                continue
            if not args.no_meta:
                if not args.quiet:
                    print(f"📦 [{i}/{total}] Fetching metadata: {pkg['package_name']}", end="\r", flush=True)
                meta = get_app_label_and_version(pkg["package_name"])
                pkg.update(meta)
            else:
                pkg["label"] = pkg["package_name"]
                pkg["version"] = "Unknown"
            apps.append(pkg)

    # Clear the progress line after the loop if it was shown
    if not args.quiet and total > 0:
        print(" " * 80, end="\r", flush=True)

    if not apps:
        print(f"{COLOR_YELLOW}⚠️ No valid packages found.{COLOR_RESET}")
        sys.exit(0)

    device_info = get_device_info()
    report_file = write_report(apps, device_info, args.format, args.output)

    print_partition_summary(apps, device_info)
    if args.verbose:
        print("\n" + generate_text_report(apps, device_info))
    print(f"\n✅ Report saved to: {COLOR_GREEN}{report_file}{COLOR_RESET}")

if __name__ == "__main__":
    main()