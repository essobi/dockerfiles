  
FROM homeassistant/home-assistant:0.59.2  
MAINTAINER Julian Kahnert <mail@juliankahnert.de>  
LABEL org.freenas.version="0.59.2" \  
org.freenas.upgradeable="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=8123 \  
org.freenas.web-ui-path="states" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.port-mappings="8123:8123/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Home-Assistant config\" \  
} \  
]"\  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"homeassistant Container Timezone\", \  
\"optional\": true \  
} \  
]"  
  
RUN pip install bs4 lxml  
  
# Bugfix  
# https://askubuntu.com/a/211531  
RUN apt-get update  
RUN apt-get install -y --force-yes apt-transport-https  
  
# Install pilight  
RUN echo "deb http://apt.pilight.org/ stable main" >
/etc/apt/sources.list.d/pilight.list  
RUN wget -O - http://apt.pilight.org/pilight.key | apt-key add -  
RUN apt-get update  
RUN apt-get install -y --force-yes pilight  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8123  

