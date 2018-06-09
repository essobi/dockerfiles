FROM alpine:edge  
MAINTAINER phasmatis  
  
ENV GID=2222 UID=990  
ENV JVM_MEMORY=512  
WORKDIR /subsonic  
  
RUN echo "@commuedge https://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk -U add \  
bash \  
ffmpeg \  
openjdk8-jre@commuedge \  
tini@commuedge \  
openssl \  
&& wget -qO- https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-6.1.3-standalone.tar.gz | tar zxf - \  
&& rm -f /var/cache/apk/*  
  
COPY start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
EXPOSE 4040  
VOLUME /config /media /playlists /podcasts  
  
LABEL description "Your complete, personal media streamer." \  
subsonic "Subsonic v6.1.1"  
  
CMD ["/sbin/tini","--","start.sh"]  

