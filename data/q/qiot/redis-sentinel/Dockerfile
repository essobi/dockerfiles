FROM redis:alpine  
  
RUN apk add --no-cache bash sed  
  
COPY sentinel.conf /usr/local/etc/redis/sentinel.conf  
COPY redis-sentinel-init.sh /usr/local/bin/redis-sentinel-init.sh  
  
EXPOSE 26379  
ENTRYPOINT [ "/usr/local/bin/redis-sentinel-init.sh" ]

