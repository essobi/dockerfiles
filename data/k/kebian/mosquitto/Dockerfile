FROM debian:jessie  
MAINTAINER robs@codexsoftware.co.uk  
  
ADD http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key /root/  
ADD http://repo.mosquitto.org/debian/mosquitto-jessie.list
/etc/apt/sources.list.d/  
RUN apt-key add /root/mosquitto-repo.gpg.key  
  
# Install mosquitto and supervisord  
RUN apt-get update && apt-get -y install mosquitto supervisor  
  
# Configure supervisord  
ADD supervisord.conf /etc/  
  
EXPOSE 1883  
ENTRYPOINT ["/usr/bin/supervisord"]

