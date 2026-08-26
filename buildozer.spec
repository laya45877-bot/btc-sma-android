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
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,openssl,certifi

# (list) Supported orientations
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_PY,NAME2:ENTRYPOINT2_PY

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (hex format)
#presplash.color = #FFFFFF

# (list) Permissions
#android.permissions = INTERNET

# (list) features
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
#android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
#android.ndk_version = 25b

# (bool) Use --private-storage data/data instead of external storage
#android.private_storage = True

# (str) Android entry point, default is ok for Kivy app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class to set as
# android entry point
#android.app_activity = --

# (list) Pattern to white list for the packaging
#android.whitelist =

# (list) List of inclusions for root directory
#android.include_exts = png,jpg,kv,atlas

# (list) List of exclusions for root directory
#android.exclude_exts = spec

# (list) List of custom Java files to add to the android project
#android.add_java_dir =

# (list) List of custom AAR files to add to the android project
#android.add_aar_dir =

# (list) List of custom Gradle dependencies to add
#android.add_gradle_dependencies =

# (list) List of pre-compiled javascript/native libraries to add
#android.add_assets =

# (list) CCache
#android.ccache = True

# (bool) Enable Android auto backup
#android.auto_backup = False

# (str) The format used to package the app for release/debug (apk or aab)
android.format = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android git clone directory (if empty, it will be automatically downloaded)
p4a.branch = master

# (str) The bootstrap to use for the app
#bootstrap = sdl2

# (int) port number to specify when to run p4a in server mode
#p4a.server_port = 8042

# (str) extra command line arguments to pass when building
#p4a.extra_args = ''

#
# To successfully build a application for Google Play, you need to accept the SDK licenses.
#
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

# (str) Path to build artifact storage, absolute or relative to spec file
#bin_dir = ./bin

# (str) Number of processes to use in parallel
#build_dir = ./.buildozer
