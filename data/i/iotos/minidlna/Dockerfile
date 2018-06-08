FROM alpine:latest  
LABEL maintainer="Iotos"  
# install minidlna  
RUN addgroup -g 100000 safeg; adduser -H -D -G safeg -s /bin/false -u 100000
safeu; apk --no-cache add minidlna; mkdir /run/db; mkdir /var/run/minidlna;
chown -R safeu:safeg /run/db; chown -R safeu:safeg /var/run/minidlna  
RUN printf
"port=8200\nmedia_dir=/opt\nalbum_art_names=Cover.jpg/cover.jpg/AlbumArtSmall.jpg/albumartsmall.jpg/AlbumArt.jpg/albumart.jpg/Album.jpg/album.jpg/Folder.jpg/folder.jpg/Thumb.jpg/thumb.jpg\ndb_dir=/run/db\ninotify=no\nenable_tivo=no\nstrict_dlna=no\nnotify_interval=900\nstrict_dlna=no\nserial=12345678\nmodel_number=1\nmax_connections=40\nfriendly_name=Media"
>> /etc/minidlna.conf  
EXPOSE 1900/udp 8200/tcp  
USER safeu:safeg  
ENTRYPOINT [ "/usr/sbin/minidlnad", "-d" ]  

