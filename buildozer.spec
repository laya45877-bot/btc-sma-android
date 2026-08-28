[app]

# (str) Title of your application
title = BTC SMA App

# (str) Package name
package.name = btcsma

# (str) Package domain (needed for android packaging)
package.domain = org.btcsma

# (str) Source where the main.py lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Version of the application
version = 0.1

# (list) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
