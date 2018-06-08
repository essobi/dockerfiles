# Dockerfile for building NetXMS webui  
FROM tomcat:8  
MAINTAINER Serhii Moroz <frost.asm@gmail.com>  
  
ENV MAJOR=2 MINOR=2 RELEASE=6  
ENV VERSION=${MAJOR}.${MINOR}.${RELEASE} NETXMS_SERVER=127.0.0.1
NETXMS_SESSIONTIMEOUT=120 NETXMS_ENABLEADVANCEDSETTINGS=true  
  
COPY ./docker-entrypoint.sh /  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
apt-get update && apt-get -y install curl apt-transport-https && \  
curl -L
https://www.netxms.org/download/releases/${MAJOR}.${MINOR}/${VERSION}/nxmc-${VERSION}.war
-o /usr/local/tomcat/webapps/nxmc.war && \  
chmod 755 /docker-entrypoint.sh  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

