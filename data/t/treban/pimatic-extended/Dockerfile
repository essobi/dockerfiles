##################################################################  
# pimatic docker file  
# VERSION 0.1  
##################################################################  
  
# base image  
FROM treban/pimatic  
  
LABEL Description="Pimatic extended docker image"
Maintainer="trebankosta@gmail.com" Version="0.1"  
  
RUN apt-get update && apt-get -y install libusb-dev and libudev-dev  
  
RUN cd /opt/pimatic-docker/ \  
# && npm install pimatic-ping \  
&& npm install pimatic-tradfri \  
&& npm install pimatic-maxcul \  
&& npm install pimatic-probe \  
&& npm install pimatic-angular-material-frontend \  
&& npm install pimatic-xmpp \  
&& npm install pimatic-alarm \  
&& npm install pimatic-kodi \  
&& npm install pimatic-led-light \  
&& npm install pimatic-mqtt \  
&& npm install pimatic-homeduino \  
&& npm install pimatic-shell-execute \  
&& npm install pimatic-sunrise \  
&& npm install pimatic-gpio \  
&& npm install pimatic-iframe \  
# && npm install pimatic-ipcamera \  
# && npm install pimatic-filebrowser \  
&& npm install pimatic-links \  
&& npm install pimatic-log-reader \  
&& npm install pimatic-wakeonlan \  
&& npm install pimatic-volkszaehler \  
&& npm install pimatic-snmp \  
&& npm install pimatic-harmonyhub \  
&& npm install pimatic-filter \  
&& npm install pimatic-hue-zll \  
&& npm install pimatic-chronotherm \  
&& npm install pimatic-mpd \  
&& npm install pimatic-telegram \  
&& npm install pimatic-echo \  
&& npm install pimatic-milight-reloaded  
  

