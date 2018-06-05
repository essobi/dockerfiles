FROM java:8-jdk-alpine  
  
RUN mkdir -p /opt \  
&& apk add --no-cache wget \  
&& wget -qO-
"https://github.com/skavanagh/KeyBox/releases/download/v2.90.02/keybox-
jetty-v2.90_02.tar.gz" \  
| tar -xzC /opt  
  
EXPOSE 8443/tcp  
VOLUME ["/a/keydb"]  
  
RUN rm /opt/KeyBox-jetty/jetty/keybox/WEB-INF/classes/jaas.conf  
ADD jaas.conf /opt/KeyBox-jetty/jetty/keybox/WEB-INF/classes/jaas.conf  
  
ADD start.sh /a/start.sh  
RUN chmod +x /a/start.sh  
  
ENTRYPOINT ["/a/start.sh"]  

