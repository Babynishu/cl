[app]
title = myapp
package.name = cal
package.domain = org.test
source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy==2.0.0,kivymd,pillow
presplash.filename = %(source.dir)s/calculatorsplash.png
icon.filename = %(source.dir)s/calculator.png
orientation = portrait

fullscreen = 0
# android.presplash_color = #FFFFFF

archs = arm64-v8a, armeabi-v7a
allow_backup = True

# (Specify any other Android-specific configurations here)

[buildozer]
log_level = 2
warn_on_root = 1
