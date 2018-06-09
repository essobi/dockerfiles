FROM talenddev/baseimage  
MAINTAINER talenddev <leo@talenddev.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Dependencies  
RUN apt-get -q update && apt-get install -qy --force-yes unzip openvpn
software-properties-common transmission-daemon  
  
# Add transmission to runit  
RUN mkdir /etc/service/transmission  
ADD start.sh /etc/service/transmission/run  
RUN chmod +x /etc/service/transmission/run  
  
EXPOSE 9091  
EXPOSE 54321  

