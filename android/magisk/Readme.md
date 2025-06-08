# Magisk Canary Downloader

This is a Python script that downloads the latest version of Magisk Canary as a ZIP file.

## Usage

1. Install Python 3.
2. Open a terminal or command prompt.
3. Navigate to the directory where you want to save the Magisk ZIP file.
4. Run the following command: `python magisk_downloader.py`

## Credits

This script was created by ChatGPT, a language model trained by OpenAI.


# magisk_download.py

## Magisk Canary Downloader

This is a simple Python script to download the latest Magisk canary build APK and make a copy converted to ZIP format.

## Dependencies

The script requires the following dependencies:

- `requests` - For making HTTP requests to download the file
- `shutil` - For copying and renaming files

Install requests using pip:

```
pip install requests
```

## Usage

To download and convert the latest canary APK:

```
python magisk_canary_downloader.py
```

This will:

- Check if the APK already exists, skip download if it does
- Download the latest canary APK from GitHub URL
- Check if converted ZIP already exists, skip conversion if it does 
- Copy and rename the APK file to ZIP format

The files created are:

- `magisk-canary.apk` - Downloaded canary APK
- `magisk-canary.zip` - Copy of APK converted to ZIP

## Customization

The following can be configured by modifying the script:

- Download URL for the canary APK
- Filenames for the APK and ZIP files

## Notes

- The script will overwrite existing APK/ZIP files on subsequent runs. 
- Checksums or signatures are not verified for the downloaded file.
- The conversion to ZIP simply renames the APK, the file contents are not changed.

## License

This script is released under the MIT License. Feel free to modify and reuse as needed.

Let me know if you would like any changes or additions to the README!