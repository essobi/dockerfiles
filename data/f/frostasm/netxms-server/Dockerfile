# Dockerfile for building NetXMS server image  
FROM debian:jessie  
MAINTAINER Serhii Moroz <frost.asm@gmail.com>  
  
ENV NETXMS_VERSION_SERVER=2.2.6-1  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
apt-get update && apt-get -y install curl apt-transport-https && \  
curl -sL http://packages.netxms.org/netxms.gpg | apt-key add - && \  
echo "deb http://packages.netxms.org/debian/ jessie main" >
/etc/apt/sources.list.d/netxms.list && \  
apt-get update && \  
apt-get -y install netcat netxms-server=$NETXMS_VERSION_SERVER netxms-dbdrv-
sqlite3=$NETXMS_VERSION_SERVER && \  
apt-get clean && \  
mkdir -p /usr/share/netxms/default-templates && \  
mv /usr/share/netxms/templates/* /usr/share/netxms/default-templates/  
  
VOLUME /data  
  
EXPOSE 4701  
EXPOSE 514/udp  
  
ENV NETXMSD_UNLOCK_ON_STARTUP=1 NETXMSD_UPGRADE_ON_STARTUP=1
NETXMSD_DEBUG_LEVEL=0  
COPY ./docker-entrypoint.sh ./wait-for /  
  
RUN chmod 755 /docker-entrypoint.sh && chmod 755 /wait-for  
  
CMD ["/docker-entrypoint.sh"]  

