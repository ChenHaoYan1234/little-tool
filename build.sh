#!/bin/sh
pyinstaller -F \
            -w \
            -i ./resource/icon.ico \
            --upx-dir ./utils/upx-4.2.2-amd64_linux/ \
            ./src/main.py