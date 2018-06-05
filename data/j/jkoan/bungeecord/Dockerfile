FROM openjdk:7-jre-alpine  
  
MAINTAINER jkoan <info@jkoan.de>  
  
#non-interactive installation  
ENV DEBIAN_FRONTEND=noninteractive BUNGEECORD_HOME=/bungeecord
SPIGOT_HOME=/minecraft SPIGOT_VER=latest  
  
COPY rootfs /  
  
RUN chmod +x /start-bungeecord.sh && adduser -s /bin/sh -D -h /bungeecord
bungeecord  
  
WORKDIR "/bungeecord"  
  
CMD /start-bungeecord.sh  
#https://docs.docker.com/engine/reference/builder/#/healthcheck  
#check status to report to dockerd  

