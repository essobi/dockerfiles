FROM java:8-jdk-alpine  
  
RUN apk update \  
&& apk add --no-cache --update ca-certificates \  
&& update-ca-certificates \  
&& apk add --no-cache wget  
  
RUN update-ca-certificates  
RUN mkdir -p /opt \  
&& wget -qO-
"https://github.com/skavanagh/KeyBox/releases/download/v2.86.00/keybox-
jetty-v2.86_00.tar.gz" \  
| tar -xzC /opt  
  
EXPOSE 8443/tcp  
VOLUME ["/a/keydb"]  
  
ADD start.sh /a/start.sh  
RUN chmod +x /a/start.sh  
  
ENTRYPOINT ["/a/start.sh"]  

