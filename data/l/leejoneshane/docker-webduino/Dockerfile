FROM node:alpine  
MAINTAINER leejoneshane@gmail.com  
  
WORKDIR /usr/src/app  
RUN apk add --no-cache git mosquitto mosquitto-clients vim \  
&& git clone https://github.com/webduinoio/webduino-blockly.git \  
&& mv webduino-blockly/* . \  
&& rm -rf webduino-blockly \  
&& npm install \  
&& sed -ri -e 's/8080/80/g' /usr/src/app/webserver.js  
  
ADD start.sh /sbin  
RUN chmod 711 /sbin/start.sh  
  
EXPOSE 80 1883  
VOLUME ["/usr/src/app"]  
CMD ["/sbin/start.sh"]  

