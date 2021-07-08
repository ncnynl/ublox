#!/usr/bin/python

import socket
import base64
import sys
import serial

dummyNMEA = "$GPGGA,035725.93,2303.8973540,N,11303.3224580,E,1,10,1.0,28.659,M,-7.659,M,0.0,0000*62"

username = "xabkf4461x"               #username for RTCM correction service
password = "xma9myekxd"                 #password for RTCM correction service
port = 8002                     #port for the service
ip = "117.135.142.201"                       #Ntrip Service IP
mountpoint = "RTCM33_GRCE"       #Ntrip Service Mountpoint
#mountpoint = ""
#Generate an encoding of the username:password for the service
auth = base64.b64encode("{}:{}".format(username, password).encode('ascii'))
auth = auth.decode('ascii')

#for serial
portx="/dev/ttyUSB1"
bps=38400
timex=5
ser=serial.Serial(portx,bps,timeout=timex)

print "Header sending... \n"

#Build Header
header =\
"GET /" + mountpoint + " HTTP/1.1\r\n" +\
"Host ip:port\r\n" +\
"Ntrip-Version: Ntrip/1.0\r\n" +\
"User-Agent: ntrip.py/0.2\r\n" +\
"Accept: */*" +\
"Connection: close\r\n" +\
"Authorization: Basic {}\r\n\r\n".format(auth)


#Start Connection + send Header
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,int(port)))
s.send(header.encode('ascii'))

print "Waiting for answer...\n"
data = s.recv(2048).decode('ascii')
print(data)
 #"Ntrip-GGA: {}".format(dummyNMEA)
#Send NMEA String
print "Sending NMEA String\n"
while True:
  print "Sending NMEA String\n"
  dummyHeader =  \
	"{}\r\n".format(dummyNMEA)
  s.send(dummyHeader)

  print "Waiting for answer...\n"

  #rtcm = s.recv(2048)
  #print(rtcm)
  ser.write(s.recv(2048))
  

ser.close()
s.close()
