FROM alpine:3.2  
MAINTAINER arckosfr <contact@lemark.xyz>  
  
ADD start.sh /usr/bin/start.sh  
ADD config.ini /tmp/config.ini  
  
VOLUME [ "/config", "/blackhole", "/torrents"]  
EXPOSE 8081  
CMD ["sh","/usr/bin/start.sh"]  
ENV TORRENT_METHOD="rtorrent" UID=5000 GID=5000  
RUN addgroup -g ${GID} torrent && adduser -h /home/torrent -s /bin/sh -D -G
torrent -u ${UID} torrent && \  
apk add --update \  
git \  
python \  
py-pip && \  
pip install \  
cheetah && \  
git clone https://github.com/SickRage/SickRage.git && chown -R torrent:torrent
/SickRage && \  
apk del py-pip && rm -rf /var/cache/apk/* && \  
chmod +x /usr/bin/start.sh

