FROM debian:jessie  
  
MAINTAINER sourceperl <loic.celine@free.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y wget  
  
RUN wget -q -O - http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key |
apt-key add -  
RUN wget -q -O /etc/apt/sources.list.d/mosquitto-jessie.list
http://repo.mosquitto.org/debian/mosquitto-jessie.list  
RUN apt-get update  
RUN apt-get install -y mosquitto  
COPY etc/mosquitto/conf.d/ /etc/mosquitto/conf.d/  
  
EXPOSE 1883 9001  
CMD /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf  

