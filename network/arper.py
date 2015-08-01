#-*- coding: utf-8 -*-
#!/usr/bin/env python

form scapy.all import *
import sys
import os
import threading
import signal

interface  = "wlan0"
target_ip  = ""
gateway_ip = ""
packet_count = 1000


