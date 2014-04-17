#!/usr/bin/env python
#
# Simple script to read out data from Galileo Serial and publish to MQTT
# broker.
#

# Import some necessary libraries.
# import socket, ssl, sys
import serial, time
import threading, os
import paho.mqtt.client as paho
mqttc = paho.Client("sensor_pub")


def mqttc_message(mosq, obj, msg):
  print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload: "+msg.payload)
  mqttc.unsubscribe("test/t006")

def mqttc_unsubscribe(mosq, obj, mid):
  print("Unsubscribe with mid "+str(mid)+" received.")
  mqttc.disconnect()

def mqttc_publish(mosq, obj, mid):
  print("Message "+str(mid)+" published.")

def mqttc_log(mosq, obj, level, string):
  print("Verbose: " +string)

if __name__=='__main__':
  mqttc.on_message = mqttc_message
  mqttc.on_unsubscribe = mqttc_unsubscribe
  mqttc.connect("115.28.241.58")

  while 1:
    mqttc.publish("/shit","{\"device\":\"temperature\"}")
    mqttc.loop(0)
    time.sleep(1)




