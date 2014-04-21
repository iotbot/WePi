#!/usr/bin/env python
#
# Simple script to read out data from Galileo Serial and publish to MQTT
# broker.
#

# Import some necessary libraries.
# import socket, ssl, sys
import time
import threading, os
import paho.mqtt.client as paho
mqttc = paho.Client("sensor_pub")
from collections import OrderedDict

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

def CPUinfo():
	CPUinfo = OrderedDict()
	procinfo = OrderedDict()
	nprocs = 0
	with open('/proc/cpuinfo') as f:
		for line in f:
			if not line.strip():
				#end of one processor
				CPUinfo['proc%s'%nprocs] = procinfo
				nprocs = nprocs + 1
				procinfo = OrderedDict()
			else:
				if len(line.split(':')) == 2:
					procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
				else:
					procinfo[line.split(':')[0].strip()] = ''
	return CPUinfo

if __name__=='__main__':
  mqttc.on_message = mqttc_message
  mqttc.on_unsubscribe = mqttc_unsubscribe
  mqttc.connect("115.28.241.58")
  CPUinfo = CPUinfo()
  while 1:
    mqttc.publish("/shit","{\"temp\":\"35.0\"}")
    #CPUinfo = CPUinfo()
    cpu_pub = ''
    for processor in CPUinfo.keys():
      cpu_pub = cpu_pub + CPUinfo[processor]['Processor']
    mqttc.publish("/cpu","{\"cpu\":\""+cpu_pub+"\"}")
    mqttc.loop(0)
    time.sleep(1)




