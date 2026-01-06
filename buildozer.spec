[app]
title = Water Inventory
package.name = waterinventory
package.domain = org.water

source.dir = .
source.include_exts = py,kv

requirements = python3,kivy,requests

orientation = portrait

[buildozer]
log_level = 2

[app.android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
