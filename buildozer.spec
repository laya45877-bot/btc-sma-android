[app]

# (str) Title of your application
title = Crypto App

# (str) Package name
package.name = cryptoapp

# (str) Package domain (needed for android packaging)
package.domain = org.crypto

# (str) Source directory where your app lives
source.dir = .

# (list) Source files to include (let it include python, png, kv, json, etc.)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it exclude disallowed files)
source.exclude_exts = spec

# (list) List of directory to include (from root of your app)
source.include_dirs = assets,images

# (list) List of exclusions
source.exclude_dirs = tests, bin, venv

# (list) Application requirements
# pip မှ ဗားရှင်းတိကျစွာ ရှာမတွေ့သည်များကို ရှောင်ရှားရန် ဗားရှင်းနံပါတ်များကို ဖြုတ်ထားပါ
requirements = python3,kivy,certifi,urllib3,idna,charset-normalizer,requests

# (str) Version of the application
version = 0.1

# (list) Application permissions
android.permissions = INTERNET

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

#
# -----------------------------------------------------------------------
# Android-specific settings

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Automatically accept Android SDK license
android.accept_sdk_license = True

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (list) Architectural build to support
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable/disable logcat printing
android.logcat_filters = *:S python:D

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact, storage, etc.
bin_dir = ./bin
