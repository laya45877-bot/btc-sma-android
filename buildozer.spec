[app]

# (str) Title of your application
title = Trade Ai, Help for you

# (str) Package name
package.name = tradeaihelpyou

# (str) Package domain (needed for android packaging)
package.domain = org.tradeai

# (str) Source where the main.py lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Version of the application
version = 0.1

# (list) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible
android.api = 31

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 31

# (str) ANT version to use
# android.ant_version = 1.9.4

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
