FROM nginx:stable-alpine  
  
RUN apk --no-cache add ca-certificates wget tar \  
&& wget -O freeboard.tar.gz
https://api.github.com/repos/Freeboard/freeboard/tarball/master \  
&& tar -xzvf freeboard.tar.gz -C /usr/share/nginx/html \--strip-components=1  
  
COPY paho.mqtt.plugin.js /usr/share/nginx/html/plugins/thirdparty/  
COPY mqttws31.js /usr/share/nginx/html/plugins/mqtt/  
COPY index.html /usr/share/nginx/html/  
COPY dashboard.json /usr/share/nginx/html/  

