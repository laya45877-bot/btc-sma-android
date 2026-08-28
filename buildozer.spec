[app]

# (str) Title of your application
title = TradeAi

# (str) Package name
package.name = tradeai

# (str) Package domain (needed for android packaging)
package.domain = org.tradeai

# (str) Source where the main.py lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
requirements = python3,kivy

# (str) Application versioning
version = 0.1

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (bool) Use the AndroidX support library
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (str) Path to build artifact, relative to the spec file
bin_dir = bin
