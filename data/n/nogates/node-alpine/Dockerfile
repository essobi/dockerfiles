FROM node:alpine  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-mappings="4200:4200/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/app\", \  
\"descr\": \"application folder\" \  
} \  
]"  
  
RUN npm install -g ember-cli runjs  
  
ENV LAUNCHER_DIR /usr/local/bin  
  
WORKDIR $LAUNCHER_DIR  
  
VOLUME ["/app"]  
  
EXPOSE 4200  
  
COPY ./start_app.sh $LAUNCHER_DIR  
  
ENTRYPOINT $LAUNCHER_DIR/start_app.sh  

