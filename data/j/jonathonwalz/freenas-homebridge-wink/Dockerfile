FROM node:6-alpine  
  
COPY package.json package.json  
  
RUN \  
apk add --no-cache --update avahi dbus make gcc g++ python avahi-dev avahi-
compat-libdns_sd supervisor && \  
npm config set progress false && \  
npm install --production && \  
npm cache clean && \  
apk del make gcc g++ python avahi-dev  
COPY supervisord.conf /etc/supervisord.conf  
  
VOLUME /root/.homebridge  
EXPOSE 5353/udp 51826/tcp  
  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1.01" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-mappings="5353:5353/udp,51826:51826/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/root/.homebridge\", \  
\"descr\": \"Config storage location\" \  
} \  
]"  
  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisord.conf"]

