[app]
# App name (human-readable title)
title = Tehrik-e-Jadid Tracker

# Source directory (path to your Python code)
source.dir = .

# Package name
package.name = org.mkaug

# Version (e.g., 1.0.0)
version = 1.0.0

# App orientation (portrait/landscape)
orientation = portrait

# Kivy version (match your installed version)
requirements = python3,kivy==2.3.1,kivymd,firebase-admin,openpyxl,pyjnius

# Android permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, RECEIVE_BOOT_COMPLETED, WRITE_EXTERNAL_STORAGE

# Icon (create a 512x512 PNG icon and place it in the project folder)
icon = icon.png

# (str) The name of the entry point for your application.
entrypoint = main.py

# Android specific
target = android  # Add this line

android.sdk_path = C:\Users\rxs\AppData\Local\Android\Sdk
android.ndk_path = C:\Users\rxs\AppData\Local\Android\Sdk\ndk\<version>  # Replace <version> with the installed version number
android.accept_sdk_license = True
android.api = 33

# (bool) Skip android.sdk installation
android.skip_update = False

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.minapi = 21
