# 📱 Android App Lister via ADB

![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A powerful, cross-platform Python CLI tool designed to list **all installed Android apps** on your device—including **system**, **user**, **vendor**, and other partitioned apps. Ideal for device auditing, app analysis, or simply gaining a full overview of your Android environment.

---

## 🚀 Key Features

- **Comprehensive App Listing**  
  Enumerates applications from **all** Android partitions: `user`, `system`, `vendor`, `product`, `odm`, etc., providing a complete overview.

- **Detailed App Metadata**  
  Collects package name, APK path, partition type, version, and human-readable label (e.g., “Google Chrome” instead of `com.android.chrome`).

- **Device Information**  
  Displays manufacturer, model, and Android version of the connected device.

- **Flexible Output Formats**  
  Export reports in `.txt` (plain text), `.json` (structured), or `.csv` (spreadsheet-friendly).

- **Interactive Console Summary**  
  View a colorized breakdown of app counts by partition, printed directly in your terminal.

- **Optimized Performance**  
  Use `--no-meta` to skip metadata (label/version) collection and scan apps faster.

- **Quiet or Verbose Output**  
  `--quiet` for minimal output, or `--verbose` to display the full report in your terminal.

- **Partition Filtering**  
  Use `--partition` to limit output to specific partitions (`user`, `system`, `vendor`, etc.).

- **Custom Report File Path**  
  Save results to a file path of your choosing with `--output`.

---

## 🛠️ Requirements

- **Python 3.6+**
- **ADB (Android Debug Bridge)** installed and in your system PATH

Verify ADB is available:
```bash
adb version
# Expected output similar to: Android Debug Bridge version 1.0.41

If ADB is not found, download the Android Platform-Tools:  
https://developer.android.com/studio/releases/platform-tools
````

* An Android device with **USB debugging enabled**

---

## 📦 Installation

1. **Download this script:**

   ```bash
   curl -O https://raw.githubusercontent.com/HelllGuest/python_scripts/main/android/apps/list_installed_android_apps.py
   ```
   OR

    ```bash
   wget https://raw.githubusercontent.com/HelllGuest/python_scripts/main/android/apps/list_installed_android_apps.py
    ```

2. **(Optional) Make the script directly executable:**

   ```bash
   chmod +x list_installed_android_apps.py
   # You can then run it directly like: ./list_installed_android_apps.py
   ```

3. **Run the script:**

   ```bash
   python list_installed_android_apps.py
   ```

---

## 📋 Usage

### 🔍 Basic Command

```bash
python list_installed_android_apps.py
```

### ⚙️ Options

| Flag/Argument             | Description                                                        |
| ------------------------- | ------------------------------------------------------------------ |
| `--format` txt/json/csv   | Output format (default: `txt`)                                     |
| `--no-meta`               | Skip fetching app label and version for speed                      |
| `--verbose`               | Display full report in terminal                                    |
| `--quiet`                 | Suppress progress and output messages                              |
| `--partition` \[TYPES...] | Filter by one or more partitions: `user`, `system`, `vendor`, etc. |
| `--output` `<path>`       | Custom path to save the report                                     |

---

## 🧪 Examples

1. **Generate a default TXT report:**

   ```bash
   python list_installed_android_apps.py
   ```

2. **Skip metadata for a faster scan:**

   ```bash
   python list_installed_android_apps.py --no-meta
   ```

3. **Only include user apps and export to CSV:**

   ```bash
   python list_installed_android_apps.py --partition user --format csv
   ```

4. **Write report to a specific file:**

   ```bash
   python list_installed_android_apps.py --output ~/Desktop/apps_report.txt
   ```

5. **Print report in terminal (verbose mode):**

   ```bash
   python list_installed_android_apps.py --verbose
   ```

---

## 📄 Output Example (TXT)

```txt
Installed Android Apps Report - 2025-06-08 18:15:23
Device: Samsung Galaxy S21 (Android 13)
======================================================================

System Apps (58):
----------------------------------------------------------------------
Package Name   : com.android.settings
APK Path       : /system/priv-app/Settings/Settings.apk
Label          : Settings
Version        : 13.1.2
----------------------------------------------------------------------

User Apps (12):
----------------------------------------------------------------------
Package Name   : com.spotify.music
APK Path       : /data/app/~~xyz123/com.spotify.music-1/base.apk
Label          : Spotify
Version        : 8.9.12.345
----------------------------------------------------------------------

Vendor Apps (4):
...
----------------------------------------------------------------------

✅ Report saved to: installed_apps_report_20250608_181523.txt
```

---

## 🖥️ Sample Console Output

When you run the script, you'll see a quick summary of app counts by partition, color-coded for clarity:

```shell
📱 Device: Samsung Galaxy S21 (Android 13)
📦 App Summary:
  ├─ system : 58 apps
  ├─ user   : 12 apps
  ├─ vendor : 4 apps
  └─ total  : 74 apps

✅ Report saved to: installed_apps_report_20250608_181523.txt
```

---

## 🧯 Troubleshooting

| Problem              | Solution                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------- |
| ❌ ADB not found      | Ensure ADB is installed and accessible in your system PATH. Run `adb version` to verify.     |
| ❌ No device detected | Confirm USB debugging is enabled and the device is authorized on the PC.                     |
| Empty output         | Ensure apps are installed, or check that your `--partition` filter isn't overly restrictive. |
| Report not saved     | Make sure the output directory exists and you have write permissions to that location.       |

---

## 🤝 Contributing

Your feedback and contributions are always welcome!
Feel free to [open an issue](https://https://github.com/HelllGuest/python_scripts/tree/issues) or submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.
See [LICENSE](./LICENSE) for details