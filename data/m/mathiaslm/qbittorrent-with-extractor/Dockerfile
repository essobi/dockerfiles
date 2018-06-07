FROM linuxserver/qbittorrent  
  
ENV HOME="/config" -XDG_CONFIG_HOME="/config" -XDG_DATA_HOME="/config"  
RUN apk add \--no-cache p7zip tar unzip unrar  
  
COPY extract.sh /root/home/extract.sh  
  
RUN chmod +x /root/home/extract.sh  
  
EXPOSE 6881 6881/udp 8080  
  
VOLUME /config /downloads  

