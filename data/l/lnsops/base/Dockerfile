FROM alpine:latest  
  
RUN apk update && \  
apk add curl nano && \  
rm -rf /var/lib/apk/* && \  
curl -sL https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz \  
-o /tmp/s6.tgz && \  
tar xzf /tmp/s6.tgz -C / && \  
rm -f /tmp/s6.tgz  
  
ENTRYPOINT ["/init"]  
  
CMD []  

