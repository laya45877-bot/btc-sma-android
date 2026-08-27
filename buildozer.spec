[app]

# --------------------------------
# Application information
# --------------------------------

title = BTC SMA App

package.name = btcsma

package.domain = org.btcsma

version = 0.1


# --------------------------------
# Source
# --------------------------------

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,csv,txt,ttf,otf


# --------------------------------
# Exclude unnecessary files
# --------------------------------

source.exclude_dirs = .git,bin,.buildozer,venv,tests,__pycache__


# --------------------------------
# Python requirements
# --------------------------------

requirements = python3,kivy,pyjnius


# --------------------------------
# Android permissions
# --------------------------------

android.permissions = INTERNET


# --------------------------------
# Screen orientation
# --------------------------------

orientation = portrait


# --------------------------------
# Android storage
# --------------------------------

android.private_storage = True


# --------------------------------
# Android architectures
# --------------------------------

android.archs = arm64-v8a,armeabi-v7a


# --------------------------------
# Android API
# --------------------------------

android.api = 33

android.minapi = 21


# --------------------------------
# Android NDK
# --------------------------------

android.ndk = 25b


# --------------------------------
# Android build
# --------------------------------

p4a.bootstrap = sdl2

android.accept_sdk_license = True


# --------------------------------
# Python for Android
# --------------------------------

p4a.branch = master


# --------------------------------
# Buildozer settings
# --------------------------------

[buildozer]

log_level = 2

warn_on_root = 1
