FROM alpine:latest  
MAINTAINER WOOLAN <WOOLAN@piratized.se>  
  
RUN apk add --no-cache rtorrent \  
&& mkdir /downloads \  
&& mkdir -p /rtorrent/.session  
  
ADD rootfs/rtorrent.rc /rtorrent/.rtorrent.rc  
  
# Declare ports to expose (SCGI, DHT, listen)  
EXPOSE 5000 9527 45566  
# Declare volumes  
VOLUME ["/rtorrent", "/downloads"]  
  
# Command  
CMD ["rtorrent", "-n", "-o", "import=/rtorrent/.rtorrent.rc"]  

