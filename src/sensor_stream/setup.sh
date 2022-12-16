#!/bin/bash

if [[ ! $1 =~ /lib$ ]]; then
    # Exit if the first argument doesn't end in "/lib"
    echo "usage: ./setup.sh /path/to/bundle/lib"
    exit 1
fi

CIRCUITPY=${2:-/Volumes/CIRCUITPY}
mkdir -p $CIRCUITPY/lib

cd $1

cp adafruit_clue.mpy $CIRCUITPY/lib
cp neopixel.mpy $CIRCUITPY/lib
cp -r adafruit_apds9960 $CIRCUITPY/lib/adafruit_apds9960
cp adafruit_bmp280.mpy $CIRCUITPY/lib
cp adafruit_lis3mdl.mpy $CIRCUITPY/lib
cp -r adafruit_register $CIRCUITPY/lib/adafruit_register
cp -r adafruit_lsm6ds $CIRCUITPY/lib/adafruit_lsm6ds
cp adafruit_sht31d.mpy $CIRCUITPY/lib
cp -r adafruit_display_text $CIRCUITPY/lib/adafruit_display_text
cp -r adafruit_ble $CIRCUITPY/lib/adafruit_ble
