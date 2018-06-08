FROM nordstrom/java:8  
MAINTAINER Innovation Platform Team "invcldtm@nordstrom.com"  
ENV GOCD_VERSION=16.2.1-3027 \  
DOCKER_VERSION=1.9.1  
ADD gocd-gpg-key.asc /tmp/  
RUN echo "deb https://download.go.cd /" > /etc/apt/sources.list.d/gocd.list \  
&& apt-key add /tmp/gocd-gpg-key.asc  
  
RUN apt-get update -qy \  
&& apt-get install -qy \  
git \  
go-server=${GOCD_VERSION}  
  
EXPOSE 8153 8154  
ADD cruise-config.xml log4j.properties /etc/go/  
RUN chown go:go /etc/go/*  
  
ENV MANUAL_SETTING=Y \  
DAEMON=N \  
SERVER_WORK_DIR=/var/lib/go-server \  
GO_SERVER_PORT=8153 \  
GO_SERVER_SSL_PORT=8154  
USER go  
  
ENTRYPOINT ["/usr/share/go-server/server.sh"]  

