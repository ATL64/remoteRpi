This repository contains scripts to record and send signals for 433Mhz radio frequency remote controls (will obviously not work with infrared remotes).  The docker version is to be run on the RaspberryPi with docker installed in it, and can only be used to SEND signals with a transmitter.  To READ signals, you need to simply install and run the scripts on the RPi itself.

With this you can "hack" remote controls, i.e. decode their frequencies for specific commands, and then emit them using your RaspberryPi connected to a transmitter.

Signals to test with my intertechno remote for home:

first on
`279 2759 279 279 279 1333 279 1333 310 248 279 279 279 1333 279 1333 279 310 279 279 279 1364 279 1333 248 310 279 1333 248 279 279 279 279 1364 279 310 248 1333 279 1333 279 279 279 310 248 1364 248 279 279 1364 248 279 279 1364 248 310 248 1364 279 1364 248 310 279 1364 248 310 248 279 248 1364 248 1333 248 310 248 1333 248 310 279 310 248 1364 248 341 217 1364 279 1333 248 310 279 1333 248 310 279 310 248 1364 248 1364 279 279 248 279 279 1364 248 279 279 1364 248 1364 248 310 248 279 279 1364 248 310 248 1364 248 310 279 1364 248 341 217 1364 248 10602`

first off
`248 2790 248 279 279 1364 310 1302 279 310 248 279 279 1364 248 1333 248 279 279 310 248 1364 248 1364 248 310 248 1333 279 310 279 279 279 1364 248 310 248 1364 279 1333 248 310 248 279 279 1364 248 310 248 1364 279 279 279 1364 248 310 248 1426 186 1333 279 310 279 1364 279 279 279 310 248 1364 248 1333 248 310 248 1364 248 310 248 310 248 1364 248 310 248 1364 248 1364 248 310 279 1364 248 310 248 310 248 1364 248 1364 248 341 248 310 248 1364 248 310 248 1364 248 310 248 1395 248 310 248 1364 248 310 248 1364 248 310 248 1364 248 310 248 1364 248 10602`

Very basic outline here:

https://hackernoon.com/diy-home-automation-fan-control-with-raspberry-pi-3-rf-transmitter-and-homebridge-59ad24845770

Test transmission script:

`sh discolights`


Listen to signals:

`sudo killall pilight-daemon`

`sudo pilight-debug`

To send signals:

`sudo pilight-daemon`

`sudo pilight-send -p raw -c "248 2790 248 279 279 1364 310 1302 279 310 248 279 279 1364 248 1333 248 279 279 310 248 1364 248 1364 248 310 248 1333 279 310 279 279 279 1364 248 310 248 1364 279 1333 248 310 248 279 279 1364 248 310 248 1364 279 279 279 1364 248 310 248 1426 186 1333 279 310 279 1364 279 279 279 310 248 1364 248 1333 248 310 248 1364 248 310 248 310 248 1364 248 310 248 1364 248 1364 248 310 279 1364 248 310 248 310 248 1364 248 1364 248 341 248 310 248 1364 248 310 248 1364 248 310 248 1395 248 310 248 1364 248 310 248 1364 248 310 248 1364 248 310 248 1364 248 10602"`

`sh discolights`

Might give an error if not connected to internet (to be looked into).

The config.json goes to the following path

`sudo nano /etc/pilight/config.json`

The sender and receiver of the config.json must use wiringX numeration of the pins as shown in the image.

For docker, go to the dockerfile directory,

`docker build . pilight:8.0.2`

and then

`docker run \
-d \
-v /etc/pilight/config.json:/etc/pilight/config.json \
--cap-add SYS_RAWIO \
--device /dev/mem \
pilight:8.0.2`

