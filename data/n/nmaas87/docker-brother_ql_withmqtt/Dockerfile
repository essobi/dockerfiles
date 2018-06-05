FROM nmaas87/docker-brother_ql:latest  
MAINTAINER Nico Maas <mail@nico-maas.de>  
ENV DEBIAN_FRONTEND noninteractive  
RUN [ "cross-build-start" ]  
# Installing MQTT  
RUN curl -O http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key && \  
apt-key add mosquitto-repo.gpg.key && \  
rm mosquitto-repo.gpg.key && \  
cd /etc/apt/sources.list.d/ && \  
curl -O http://repo.mosquitto.org/debian/mosquitto-stretch.list && \  
apt-get update && \  
apt-get install -y mosquitto mosquitto-clients && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir /var/lib/apt/lists/partial && \  
/etc/init.d/mosquitto stop && \  
pip install paho-mqtt --no-cache-dir  
#ENTRYPOINT ["/usr/bin/tail", "-f", "/etc/hosts"]  
RUN [ "cross-build-end" ]

