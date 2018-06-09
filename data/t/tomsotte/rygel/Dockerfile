FROM ubuntu:xenial  
MAINTAINER tomsotte@gmail.com  
LABEL \  
Description="Rygel DLNA/uPNP server docker image" \  
Vendor="GNOME" \  
Version="latest"  
  
ENV RYGEL_CACHE_DIR=/root/.cache/rygel \  
RYGEL_VIDEOS_DIR=/videos \  
RYGEL_MUSIC_DIR=/music \  
RYGEL_PICTURES_DIR=/pictures  
  
RUN apt-get update; \  
apt-get upgrade -y; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
rygel; \  
rm -rf /var/lib/apt/lists/*;  
  
COPY rygel.conf /root/.config/  
  
EXPOSE 8000/tcp 1900/udp  
  
VOLUME ["${RYGEL_CACHE_DIR}", "${RYGEL_VIDEOS_DIR}", "${RYGEL_MUSIC_DIR}",
"${RYGEL_PICTURES_DIR}"]  
  
CMD ["/usr/bin/rygel"]  

