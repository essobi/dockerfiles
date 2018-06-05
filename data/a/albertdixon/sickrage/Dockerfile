FROM alpine:3.4  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
VOLUME ["/data"]  
ENTRYPOINT ["tini", "--", "/sbin/entry"]  
CMD ["/sbin/start"]  
EXPOSE 8081  
ENV LANGUAGE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
OPEN_FILE_LIMIT=32768 \  
PATH=/src/sickrage:$PATH \  
REPO=SickRage/SickRage \  
SB_CHANNEL=master \  
SB_DATA=/data \  
SB_GID=7000 \  
SB_HOME=/src/sickrage \  
SB_PORT=8081 \  
SB_UID=7000 \  
SB_USER=sickrage \  
UPDATE_INTERVAL=1h \  
LANG=en_US.UTF-8  
ADD
https://github.com/albertrdixon/escarole/releases/download/v0.2.3/escarole-
linux.tgz /es.tgz  
COPY ["entry", "start", "/sbin/"]  
COPY escarole.yml /  
  
RUN mkdir -v /torrents /tv_shows /downloads \  
&& chmod +rx /sbin/entry /sbin/start \  
&& tar xvzf /es.tgz -C /bin \  
&& echo "http://dl-4.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --update --purge \  
ca-certificates \  
git \  
libxml2 \  
openssl \  
py-html5lib \  
py-libxml2 \  
py-lxml \  
py-mako \  
py-openssl \  
py-pillow \  
python \  
tini \  
unrar \  
unzip \  
&& rm -rf /es.tgz  

