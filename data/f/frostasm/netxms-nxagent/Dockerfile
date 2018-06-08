# Dockerfile for building NetXMS server image  
FROM debian:jessie  
MAINTAINER Serhii Moroz <frost.asm@gmail.com>  
  
ENV NETXMS_VERSION_AGENT=2.2.6-1  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
apt-get update && apt-get -y install curl apt-transport-https && \  
curl -sL http://packages.netxms.org/netxms.gpg | apt-key add - && \  
echo "deb http://packages.netxms.org/debian/ jessie main" >
/etc/apt/sources.list.d/netxms.list && \  
apt-get update && \  
apt-get -y install libssh-4 && \  
apt-get -y install netxms-agent=$NETXMS_VERSION_AGENT && \  
apt-get clean  
  
VOLUME /data  
  
EXPOSE 4700  
COPY ./ssh.nsm /usr/lib/x86_64-linux-gnu/netxms/  
COPY ./docker-entrypoint.sh /  
  
RUN chmod 755 /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

