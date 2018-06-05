FROM gliderlabs/alpine:latest  
  
RUN apk update && \  
apk add socat && \  
rm -f /var/cache/apk/APKINDEX*  
  
ADD run.sh /run.sh  
  
CMD ["/run.sh"]  

