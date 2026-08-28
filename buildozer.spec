[app]

# (str) Title of your application
title = BTC SMA App

# (str) Package name
package.name = btcsma

# (str) Package domain (needed for android packaging)
package.domain = org.btcsma

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# (ကိုယ့် App မှာသုံးထားတဲ့ Library တွေပေါ်မူတည်ပြီး ထည့်ပါ)
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (NOTE: android.sdk ဆိုတာကို ဖယ်ရှားပြီးပါပြီ - Warning တက်တာ ပျောက်စေရန်)
