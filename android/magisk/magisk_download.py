import os
import sys
import shutil
import requests

url = "https://raw.githubusercontent.com/topjohnwu/magisk-files/canary/app-debug.apk"
apk_file = "magisk-canary.apk"
zip_file = "magisk-canary.zip"

if os.path.exists(apk_file):
    print("APK file already exists.")
    
    if os.path.exists(zip_file):
        print("ZIP file already exists. Skipping copy.")
    else:
        print("Copying APK to ZIP...")
        shutil.copy2(apk_file, zip_file)
        print("ZIP copy created.")
        
else:
    print("Downloading Magisk canary...")
    response = requests.get(url)
    with open(apk_file, 'wb') as file:
        file.write(response.content)

    print("Download finished!")
    
    print("Copying APK to ZIP...")
    shutil.copy2(apk_file, zip_file)
    print("ZIP copy created.")