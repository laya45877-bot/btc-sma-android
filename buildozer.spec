[app]

# (str) Title of your application
title = BTC SMA App

# (str) Package name
package.name = btcsma

# (str) Package domain (needed for android packaging)
package.domain = org.btcsma

# (str) Source where the app is located
source.dir = .

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it blank to exclude nothing)
#source.exclude_exts = spec

# (list) List of directory to exclude (let it blank to exclude nothing)
#source.exclude_dirs = tests, bin, venv

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pyjnius

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientations
orientation = portrait

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b
