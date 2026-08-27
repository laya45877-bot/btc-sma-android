[app]

title = BTC SMA App
package.name = btcsma
package.domain = org.btcsma

# Creator / Author
author = Kyaw Thet Aung (Zeyo)

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,pyjnius

android.permissions = INTERNET

orientation = portrait

android.private_storage = True

android.archs = arm64-v8a, armeabi-v7a

android.api = 33
android.minapi = 21
android.ndk = 25b

android.accept_sdk_license = True

# (str) python-for-android branch to use (stable branch ကို သုံးရန်)
p4a.branch = release
