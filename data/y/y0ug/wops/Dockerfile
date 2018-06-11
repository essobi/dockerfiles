# Set the base image to Ubuntu  
FROM y0ug/base-ws  
  
# File Author / Maintainer  
MAINTAINER y0ug  
  
RUN apt-get update && apt-get upgrade -yq  
  
RUN apt-get install -yq \  
iptables openvpn \  
mingw-w64 mingw32 binutils-mingw-w64 \  
cadaver vncsnapshot proxychains tsocks \  
polipo privoxy samba firefox  
  
RUN pip install --upgrade pip netifaces requests  
RUN pip install impacket  
  
RUN mkdir -p /var/tools/ && chown y0ug:y0ug /var/tools  
ADD install.sh /tmp/  
USER y0ug  
RUN /tmp/install.sh  
USER root  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 22  
VOLUME ['/var/log', '/home/y0ug',]  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

