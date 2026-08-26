[app]

# (str) Title of your application
title = BTC SMA Bot by Kyaw Thet Aung(Zeyo)

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
# ဒီနေရာမှာ လိုအပ်မယ့် libraries တွေ အားလုံးကို ကော်မာ (,) ခံပြီး ထည့်ပေးရပါမယ်
requirements = python3,kivy
# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (list) Android architectural support (arm64-v8a, armeabi-v7a, x86, x86_64)
android.archs = arm64-v8a

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
