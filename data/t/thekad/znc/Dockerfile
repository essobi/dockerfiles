FROM docker.io/alpine:latest  
  
ENV SSL_PEM=/ssl/znc.pem  
  
RUN apk update && \  
apk add dumb-init g++ znc znc-dev znc-extra ca-certificates  
  
ADD entrypoint.sh /entrypoint.sh  
ADD znc.conf.default /znc.conf.default  
  
# Cheat a little bit, we need to let apk run even with --user  
RUN mkdir -pv /ssl /data/configs && \  
chmod -Rv 0775 /data /ssl && \  
chmod u+s /sbin/apk  
  
VOLUME ["/data"]  
VOLUME ["/ssl"]  
  
EXPOSE 6667  
ENTRYPOINT ["/usr/bin/dumb-init"]  
CMD ["/entrypoint.sh"]  

