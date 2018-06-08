FROM alpine:edge  
  
MAINTAINER arckosfr <contact@lemark.xyz>  
  
LABEL version="201608101" \  
tags="latest"  
  
ENV GID=991 UID=991  
WORKDIR /madsonic  
  
RUN echo "@commuedge https://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk -U add \  
ffmpeg \  
openjdk8-jre@commuedge \  
tini@commuedge \  
&& wget -qO-
http://madsonic.org/download/6.1/20160505_madsonic-6.1.8280-standalone.tar.gz
| tar zxf - \  
&& rm -f /var/cache/apk/*  
  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
EXPOSE 4040  
VOLUME /data /musics /playlists /podcasts  
  
CMD ["/sbin/tini","--","run.sh"]  

