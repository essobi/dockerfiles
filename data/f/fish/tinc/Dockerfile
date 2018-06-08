FROM ubuntu:trusty  
MAINTAINER Johannes 'fish' Ziemke <docker@freigeist.org>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y -q install tinc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
EXPOSE 655  
EXPOSE 655/udp  
VOLUME /tinc  
  
ENTRYPOINT [ "tincd", "-D", "-c", "/tinc", "-U", "nobody" ]  

