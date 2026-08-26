[app]

# (str) Title of your application
title = BTC SMA Bot

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

# (list) Application requirements (ဒီနေရာမှာ APK ပေါ့ပါးအောင် လိုအပ်တာတွေပဲ ချုံ့ထားပါတယ်)
requirements = python3,kivy,openssl,certifi
# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (list) Android architectural support
android.archs = arm64-v8a

# (bool) If True, automatically accept SDK license
android.accept_sdk_license = True

# NDK version ကို 25b သို့ တိကျစွာ သတ်မှတ်ပေးခြင်း
android.ndk = 25b

# python-for-android branch to use
p4a.branch = master

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to build artifact, storage, etc.
build_dir = .buildozer

# (str) Path to output bin (APK, AAB)
bin_dir = ./bin
