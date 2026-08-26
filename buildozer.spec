[app]

# (str) Title of your application
title = BTC SMA Bot by Kyaw Thet Aung (Zeyo)

# (str) Package name
package.name = btcsma

# (str) Package domain (needed for android packaging)
package.domain = org.example

# (list) Source files to include (let it empty to include all files)
source.dir = .

# (list) List of extensions to pack
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,openssl,certifi

# (list) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk_version = 25b

# (str) The format used to package the app for release/debug (apk or aab)
android.format = apk

#
# Python for android (p4a) specific
#
p4a.branch = master

#
# To successfully build a application for Google Play, you need to accept the SDK licenses.
#
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
