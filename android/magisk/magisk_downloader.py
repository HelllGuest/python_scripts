import urllib.request
import os

# URL for the Magisk Canary APK file
url = "https://raw.githubusercontent.com/topjohnwu/magisk-files/canary/app-debug.apk"

# Set the desired filenames for the APK and ZIP files
apk_filename = "magisk.apk"
zip_filename = "magisk.zip"

# Check if the ZIP file already exists and display a message if it does
if os.path.exists(zip_filename):
    print(f"{zip_filename} already exists.")
else:
    # Download the APK file
    print(f"Downloading {url}...", end="", flush=True)
    urllib.request.urlretrieve(url, apk_filename, reporthook=lambda x,y,z: print(f"\rProgress: {int(y/z*100)}%", end="", flush=True), data=None)
    print("\rDownload complete.")

    # Make a copy of the APK file and rename it to ZIP
    print(f"Copying {apk_filename} to {zip_filename}...", end="", flush=True)
    with open(apk_filename, "rb") as apk_file, open(zip_filename, "wb") as zip_file:
        zip_file.write(apk_file.read())
    os.rename(zip_filename, zip_filename)
    print("\rCopy and rename complete.    ")
