FROM debian:jessie  
MAINTAINER Christophe Burki, christophe.burki@gmail.com  
  
# Install system requirements  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
locales \  
wget && \  
apt-get autoremove -y && \  
apt-get clean  
  
# Configure locales and timezone  
RUN locale-gen en_US.UTF-8 en_GB.UTF-8 fr_CH.UTF-8 && \  
cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime && \  
echo "Europe/Zurich" > /etc/timezone  
  
# Install mosquitto clients  
RUN wget -q -O /tmp/mosquitto-repo.gpg.key
http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key && \  
apt-key add /tmp/mosquitto-repo.gpg.key && \  
wget -q -O /etc/apt/sources.list.d/mosquitto-jessie.list
http://repo.mosquitto.org/debian/mosquitto-jessie.list && \  
apt-get update && apt-get install -y mosquitto-clients  
  
# No ENTRYPOINT nor CMD !  
# One of mosquitto_pub or mosquitto_sub must be given when running the imgage.  

