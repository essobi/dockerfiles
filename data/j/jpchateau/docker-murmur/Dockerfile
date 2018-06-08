FROM debian:jessie  
  
MAINTAINER Jean-Philippe Chateau "contact@jpchateau.com"  
ENV MURMUR_VERSION 1.2.19  
VOLUME ["/data"]  
  
WORKDIR /murmur  
  
RUN apt-get update && \  
apt-get install -y \  
apt-utils \  
wget bzip2 && \  
rm -rf /var/lib/apt/lists/*; \  
wget -O murmur.tar.bz2 https://github.com/mumble-
voip/mumble/releases/download/$MURMUR_VERSION/murmur-
static_x86-$MURMUR_VERSION.tar.bz2; \  
tar -xjf murmur.tar.bz2 && \  
rm murmur.tar.bz2 && \  
mv murmur-static_x86-$MURMUR_VERSION/* ./ && \  
rmdir murmur-static_x86-$MURMUR_VERSION; \  
apt-get purge -y --auto-remove \  
apt-utils \  
wget \  
bzip2  
  
COPY config/murmur.ini.sample .  
COPY start.sh /  
  
EXPOSE 64738/tcp 64738/udp  
  
CMD ["/start.sh"]

