FROM alpine:latest  
  
RUN apk add --update redis && \  
rm -rf /var/cache/apk/* && \  
mkdir /data && \  
chown 1001:0 /data && \  
chmod ug+rw /data  
  
VOLUME /data  
WORKDIR /data  
  
USER 1001  
EXPOSE 6379  
CMD ["redis-server"]  

