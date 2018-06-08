FROM phusion/baseimage:0.9.16  
MAINTAINER Ian blenke <ian@blenke.com>  
  
RUN apt-get update  
RUN apt-get -y -q install libpcap0.8  
  
RUN curl -L -o /tmp/packetbeat_amd64.deb
https://github.com/packetbeat/packetbeat/releases/download/v0.4.3/packetbeat_0.4.3-1_amd64.deb  
RUN dpkg -i /tmp/packetbeat_amd64.deb  
  
ADD packetbeat.conf /etc/packetbeat/packetbeat.conf  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
VOLUME /etc/packetbeat  
  
CMD /run.sh  

