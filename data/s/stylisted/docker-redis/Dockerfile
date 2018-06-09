FROM gliderlabs/alpine:3.3  
RUN apk-install curl  
  
RUN curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64"  
RUN chmod +x /usr/local/bin/gosu  
  
RUN apk-install redis  
  
# convox assembles these into a URL during `convox start`  
ENV LINK_SCHEME redis  
ENV LINK_PASSWORD password  
ENV LINK_PATH /0  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 6379  
CMD ["redis-server", "/tmp/redis.conf"]  

