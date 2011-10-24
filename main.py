'''
Created on Oct 23, 2011

@author: wblack
'''

# -*- coding: utf-8 -*-
import logging
# The multiprocessing package isn't
# part of the ASE installation so
# we must disable multiprocessing logging
logging.logMultiprocessing = 0

# Update path to point at cherrypy
import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
print current_dir
sys.path.append("/mnt/sdcard/sl4a/scripts/")
 
import android
import cherrypy

from templates import home 
 
#cherrypy.config.update("/mnt/sdcard/sl4a/scripts/AndroidServer/site_config.txt") 
droid = android.Android()
 
class Root(object):
    def __init__(self):
        self.droid = android.Android()
 
    @cherrypy.expose
    def index(self):
        self.droid.vibrate()
        return home

    @cherrypy.expose
    def take_pic(self):
        rs = self.droid.cameraCapturePicture("/mnt/sdcard/DCIM/Camera/Webcam/")     
        return str(rs)     

    @cherrypy.expose
    def location(self):
        location = self.droid.getLastKnownLocation().result
        location = location.get('network', location.get('gps'))
        return "LAT: %s, LON: %s" % (location['latitude'],
                                     location['longitude'])
 
def run():
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    droid.makeToast("Running quickstart")
    cherrypy.quickstart(Root(), '/')
 
if __name__ == '__main__':
    
    droid.makeToast("Starting webserver")
    run()
