[app]
# ------------------------------
# App basic information
# ------------------------------
title = Water Inventory
package.name = waterinventory
package.domain = org.water
version = 0.1

# ------------------------------
# Source code configuration
# ------------------------------
source.dir = .
source.include_exts = py,kv

# ------------------------------
# Python requirements
# ------------------------------
requirements = python3,kivy,requests

# ------------------------------
# App orientation
# ------------------------------
orientation = portrait

# ------------------------------
# Entry point (Kivy default)
# ------------------------------
entrypoint = main.py


[buildozer]
# ------------------------------
# Buildozer settings
# ------------------------------
log_level = 2
warn_on_root = 1


[app.android]
# ------------------------------
# Android-specific settings
# ------------------------------
android.permissions = INTERNET

# Android versions
android.api = 31
android.minapi = 21

# NDK (let buildozer manage it)
android.ndk = 25b

# Accept licenses automatically
android.accept_sdk_license = True

# IMPORTANT: Explicit SDK path for GitHub Actions
android.sdk_path = /home/runner/android-sdk

# Architecture (modern phones)
android.archs = arm64-v8a

# Enable fullscreen = False (default)
fullscreen = 0
