# CRUX based Docker image for running an MQTT Broker (mosquitto).  
#  
# Based on crux (CRUX Linux)  
#  
# VERSION: 0.0.1  
#  
# Last Updated: 20140422  
FROM crux  
MAINTAINER James Mills <prologic@shortcircuitnet.au>  
  
# Enable Contrib Ports  
RUN mv /etc/ports/contrib.rsync.inactive /etc/ports/contrib.rsync  
  
# Configure Package Manager  
RUN sed -i -e "s|^#prtdir /usr/ports/contrib|prtdir /usr/ports/contrib|"
/etc/prt-get.conf  
RUN sed -i -e "s|^# readme.*$|readme verbose|" /etc/prt-get.conf  
RUN sed -i -e "s|^# preferhigher.*$|preferhigher yes|" /etc/prt-get.conf  
RUN sed -i -e "s|^# runscripts.*$|runscripts yes|" /etc/prt-get.conf  
  
# Update Ports  
RUN ports -u && prt-get cache  
  
# Install mosquitto  
RUN prt-get depinst mosquitto  
  
VOLUME ["/etc/mosquitto']  
  
EXPOSE 1883  
EXPOSE 8883  
CMD ["/usr/sbin/mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]  

