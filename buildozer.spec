[app]

# (str) Title of your application
title = BTC SMA Bot by Kyaw Thet Aung(Zeyo)

# (str) Package name
package.name = btcsma

# (str) Package domain (needed for android packaging)
package.domain = org.example

# (list) Source files to include (let it empty to include all files)
source.dir = .

# (list) Source files to exclude (let it empty to exclude all files)
#source.exclude_exts = spec

# (list) List of global inclusions
#source.include_exts = py,png,jpg,kv,atlas

# (list) List of directory to exclude
#source.exclude_dirs = tests, bin

# (list) List of extensions to pack
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services = NAME:gsoccat:python main.py

#
# OSX Specific
#

#
# Author: PyobjC
#

osx.identifier = org.example.btcsma
osx.kivy_version = 1.9.1

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (list) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API to use.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (list) Android architectural support (arm64-v8a, armeabi-v7a, x86, x86_64)
android.archs = arm64-v8a

# (bool) If True, then skip trying to update the Android SDK
# android.skip_update = False

# (bool) If True, automatically accept SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact, storage, etc.
build_dir = .buildozer

# (str) Path to output bin (APK, AAB)
bin_dir = ./bin
