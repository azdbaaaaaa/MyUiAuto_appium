#! /bin/bash

# 某些国产手机无法通过adb devices侦测到，需要通过添加vendorId到~/.android/adb_usb.ini 目录下才可以

VendorId=`system_profiler SPUSBDataType | grep "Vendor ID" | tail -n1 | awk -F: '{print $2}' | awk '{print $1}' | tr -d " "`

echo $VendorId >>~/.android/adb_usb.ini

adb kill-server && adb start-server && adb devices