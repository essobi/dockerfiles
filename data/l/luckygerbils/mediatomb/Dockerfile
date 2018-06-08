FROM ubuntu:14.04  
MAINTAINER Sean Anastasi "sean@anasta.si"  
RUN apt-get update \  
&& apt-get -y install mediatomb-daemon  
  
ADD resources/config.xml /etc/mediatomb/config.xml  
  
VOLUME ["/var/log/mediatomb"]  
VOLUME ["/var/lib/mediatomb"]  
  
EXPOSE 49152/tcp 1900/udp  
  
ENTRYPOINT /usr/bin/mediatomb  

