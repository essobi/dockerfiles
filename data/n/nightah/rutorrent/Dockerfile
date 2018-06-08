FROM linuxserver/rutorrent  
  
# set labels  
LABEL maintainer="Nightah"  
  
# modifications  
RUN \  
echo "**** apply patch for /downloads/ ****" && \  
sed -i '7d;49,52d' /etc/cont-init.d/20-config  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config /downloads

