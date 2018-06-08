FROM xataz/rtorrent-rutorrent:filebot  
  
ENV UID=1100 \  
GID=1100 \  
WEBROOT=/ \  
PORT_RTORRENT=6881 \  
DHT_RTORRENT=on  
  
ENV FILEBOT_RENAME_METHOD="move" \  
FILEBOT_RENAME_MOVIES="{n} ({y})" \  
FILEBOT_RENAME_SERIES="{n}/Season {s}/{n} - {s00e00} - {t}" \  
FILEBOT_RENAME_ANIMES="{n}/{e.pad(3)} - {t}" \  
FILEBOT_RENAME_MUSICS="{n}/{fn}"  
  
COPY rootfs /  
VOLUME /data /config  
EXPOSE 5000  

