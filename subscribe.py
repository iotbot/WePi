#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import getpass
from optparse import OptionParser
import time,json
import paho.mqtt.client as paho
data = ""
mqttc = paho.Client("homehub_door")
def mqttc_message(mosq, obj, msg):
    global data
    data = msg.payload
    print data
def main():  #main function: initialize the parameters of bot and start the bot
    global data
    mqttc.on_message = mqttc_message
    mqttc.connect("115.28.241.58")
    mqttc.subscribe("/shit")  
    while mqttc.loop()==0 and data is "":
        pass
        	

if __name__=='__main__':
    main()
