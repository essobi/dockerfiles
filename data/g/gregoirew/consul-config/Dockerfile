FROM alpine:3.4  
ADD ./conf.d /etc/confd/conf.d  
ADD ./templates /etc/confd/templates  
ADD ./process.sh /  
RUN chmod +x /process.sh && \  
apk update && \  
apk add ca-certificates wget openssl && \  
update-ca-certificates && \  
wget
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 -O /confd && \  
chmod +x /confd  
  
VOLUME /consul  
VOLUME /persist/config/common  
VOLUME /persist/data  
  
ENTRYPOINT ["/process.sh"]  
  

