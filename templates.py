'''
Created on Oct 23, 2011

@author: wblack
'''


header = "<h1>Welcome to Wil's Android.</h1>"
nav = """
<ul>
    <li><a href='/'>Home</a></li>
    <li><a href='/location/'>Where am I?</a></li>
    <li><a href='/take_pic/'>Take a Pic</a></li>
    <li><a href='/webcam_list/'>WebCam Folder</a></li>
    <li><a href='/sys_stat/'>System Status</a></li>
</ul>
"""


home = header + nav + """
<p>You can choose from the following actions.</p>
       
<img src="images/cypress.jpg"/>    
"""

def sysStat(droid):
    html = "<dl>"
        
    out = droid.checkWifiState()
    html += "<dt>checkWifiState</dt>"
    html += "<dd>%s</dd>" %str(out)    
    
    out = droid.wifiGetConnectionInfo()
    html += "<dt>wifiGetConnectionInfo</dt>"
    html += "<dd>%s</dd>" %str(out)
    
    out = droid.getLastKnownLocation()
    html += "<dt>getLastKnownLocation</dt>"
    html += "<dd>%s</dd>" %str(out)
        
    html += "</dl>"
    return html


def dirList(list):
    """
    Given a list it returns it as an html list on the assumption is
    a directory listing
    
    """
    html ="<ul>"
    for l in list:
        html += """<li>%s</li>""" %(l)
    html += "</ul>"
    return html