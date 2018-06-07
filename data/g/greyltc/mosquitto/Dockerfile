# Arch Linux container with mosquitto  
FROM greyltc/archlinux-aur  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
  
# install mosquitto  
ADD setupMosquitto.sh /usr/sbin/setup-mosquitto  
RUN setup-mosquitto  
  
ADD runMosquitto.sh /usr/bin/run-mosquitto  
  
CMD run-mosquitto  

