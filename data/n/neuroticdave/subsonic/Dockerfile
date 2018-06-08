FROM alpine:edge  
  
ENV VER=6.0  
ENV GID=1000 UID=1000  
RUN apk -U add \  
ffmpeg \  
openjdk8-jre \  
tini \  
bash \  
&& rm -f /var/cache/apk/*  
  
WORKDIR /subsonic  
RUN wget -qO- http://subsonic.org/download/subsonic-$VER-standalone.tar.gz |
tar zxf -  
  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
EXPOSE 4040 4050  
VOLUME /data /musics /playlists /podcasts  
LABEL description "Open source media streamer" \  
subsonic "Subsonic v$VER"  
CMD ["tini","--","run.sh"]  

