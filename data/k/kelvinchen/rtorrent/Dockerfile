FROM kelvinchen/torrent-utils:latest  
  
# For rtorrent  
ENV TERM=xterm  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
screen \  
rtorrent \  
php7.0-fpm \  
php7.0-cli \  
nginx \  
ffmpeg \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure/install r(u)torrent  
RUN ln -s /config/rtorrent/rtorrent.rc ~/.rtorrent.rc \  
&& mkdir -p /var/run/php \  
&& git clone \--depth=1 \  
https://github.com/Novik/ruTorrent.git \  
/opt/rutorrent \  
&& sed -i "s/www-data/root/g" /etc/php/7.0/fpm/pool.d/www.conf  
  
VOLUME /config /data  
  
EXPOSE 80 49161 49161/udp 6881/udp  
  
COPY container-root/ /  
  
CMD ["/init"]  

