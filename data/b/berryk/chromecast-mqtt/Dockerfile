# To run:  
# docker run -d --restart unless-stopped --net=host --name chromecast-running
chromecast-mqttdocker  
FROM python:3  
MAINTAINER Keith Berry "keithwberry@gmail.com"  
WORKDIR /usr/src/app  
  
ADD https://github.com/berryk/chromecast-mqtt-connector/archive/master.tar.gz
.  
RUN gunzip -c master.tar.gz | tar xvf -  
  
RUN pip install --no-cache-dir -r ./chromecast-mqtt-connector-
master/requirements.txt  
  
COPY config.ini ./chromecast-mqtt-connector-master/.  
  
CMD [ "python", "./chromecast-mqtt-connector-master/connector.py" ]  

