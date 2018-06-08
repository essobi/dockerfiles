FROM ubuntu:14.04  
MAINTAINER Oleg Poyaganov <oleg@poyaganov.com>  
ENV REFRESHED_AT 2016-04-04-16-59  
RUN apt-get -y update && \  
apt-get install -y openvpn && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENTRYPOINT ["openvpn"]  
CMD ["--config", "/config.ovpn"]  

