FROM influxdb:alpine  
MAINTAINER benoit.herard@orange.com  
  
RUN apk \--update add git python py-pip bash ca-certificates curl uwsgi-python
nginx;\  
update-ca-certificates ; \  
apk add openssl;\  
pip install \--upgrade pip; \  
cd /usr/local;\  
git clone https://github.com/bherard/energyrecorder;\  
cd energyrecorder;\  
pip install -r recording-api/requirements.txt;\  
mv /entrypoint.sh /influx-entrypoint.sh;  
RUN curl
https://raw.githubusercontent.com/bherard/energyrecorder/master/docker/energyrecording-
api/recording-api-entrypoint.sh -o /entrypoint.sh;\  
chmod u+x /entrypoint.sh;\  
wget
https://raw.githubusercontent.com/bherard/energyrecorder/master/influx/create-
certs.sh -O /usr/local/bin/create-certs.sh;\  
chmod u+x /usr/local/bin/create-certs.sh;\  
echo DONE  
  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  

