# Arch Linux container with thingspeak server  
FROM greyltc/lamp-aur  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
  
# install thingspeak  
ADD setup-thingspeak.sh /usr/sbin/setup-thingspeak  
RUN setup-thingspeak  
  
ADD run-thingspeak.sh /usr/bin/run-thingspeak  
  
CMD run-thingspeak && sleep infinity  

