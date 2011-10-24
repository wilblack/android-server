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

import datetime as dt

from templates import home, header, nav 
from templates import dirList, sysStat
 
cherrypy.config.update("/mnt/sdcard/sl4a/scripts/AndroidServer/site_config.txt") 
droid = android.Android()
 
class Root(object):
    
    webcam_dir = "/mnt/sdcard/DCIM/Camera/Webcam/"
    
    def __init__(self):
        self.droid = android.Android()
 
    @cherrypy.expose
    def index(self):
        return home

    @cherrypy.expose
    def take_pic(self):
        now = dt.datetime.now()
        fname = dt.datetime.strftime(now,"%Y-%m-%d_%h-%i-%s.jpg")
        rs = self.droid.cameraCapturePicture("/mnt/sdcard/DCIM/Camera/Webcam/"+fname)     
        return str(rs)     
    
    @cherrypy.expose
    def webcam_list(self):
        rs = os.listdir(self.webcam_dir)
        rs = dirList(rs)
        return header + nav + rs
            
    
    @cherrypy.expose
    def location(self):
        location = self.droid.getLastKnownLocation().result
        location = location.get('network', location.get('gps'))
        return "LAT: %s, LON: %s" % (location['latitude'],
                                     location['longitude'])
        
    @cherrypy.expose
    def sys_stat(self):    
        rs = sysStat(self.droid)   
        return header + nav +rs       
        
 
def run():
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    #TODO Add IP address message.
    droid.makeToast("Running quickstart")
    cherrypy.quickstart(Root(), '/')
 
if __name__ == '__main__':
    droid.ttsSpeak("Starting webserver.")
    droid.makeToast("Starting AndroidServer")
    run()
