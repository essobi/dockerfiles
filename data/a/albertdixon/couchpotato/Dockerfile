FROM alpine:3.5  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/bin/start"]  
VOLUME ["/data"]  
EXPOSE 5050  
  
ENV ESCAROLE_VERSION=v0.2.3  
RUN echo "http://dl-5.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& echo "http://dl-5.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --update --no-cache --purge \  
ca-certificates \  
curl \  
git \  
openssl \  
py-html5lib \  
py-lxml \  
py-openssl \  
python \  
tar \  
tini \  
unrar \  
&& curl -#L
https://github.com/albertrdixon/escarole/releases/download/$ESCAROLE_VERSION/escarole-
linux.tgz | tar xvz -C /bin \  
&& apk del --purge curl \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
COPY start /bin/  
COPY escarole.yml /  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
OPEN_FILE_LIMIT=32768 \  
UPDATE_INTERVAL=1h \  
CP_CONFIG=/data/settings.conf \  
CP_DATA_DIR=/data \  
CP_GID=7000 \  
CP_HOME=/src/couchpotato \  
CP_PID_FILE=/data/couchpotato.pid \  
CP_UID=7000 \  
CP_CHANNEL=master  

