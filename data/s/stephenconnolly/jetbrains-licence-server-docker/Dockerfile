FROM anapsix/alpine-java:8_server-jre  
RUN apk update &&\  
apk add ca-certificates wget unzip && \  
update-ca-certificates && \  
wget https://download-cf.jetbrains.com/lcsrv/license-server-installer.zip && \  
unzip license-server-installer.zip -d /usr/local/bin/jb-license-server/ && \  
rm license-server-installer.zip  
  
ENV HOST=0.0.0.0 PORT=1017 USER=chxj1992  
  
# configure the port and hostname  
RUN /usr/local/bin/jb-license-server/bin/license-server.sh configure --port
$PORT \--listen $HOST  
  
# uncomment when we have determined what the proxy server is  
# RUN usr/local/bin/jb-license-server/bin/license-server.sh configure
--jetty.virtualHosts.names=proxy-server.mydomain.com  
EXPOSE $PORT  
  
# don't run as a service, but as a foreground process so docker can manage it
properly  
ENTRYPOINT ["/bin/sh", "-c", "/usr/local/bin/jb-license-server/bin/license-
server.sh run"]  

