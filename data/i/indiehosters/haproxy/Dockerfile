FROM haproxy:alpine  
  
RUN apk add --no-cache \  
bash \  
inotify-tools  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
  

