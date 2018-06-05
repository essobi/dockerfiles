FROM alpine:3.7  
MAINTAINER Robert Beal <rob@kohi.uk>  
  
ENV VERSION=0.14.47  
ENV ARCH=amd64  
ARG UID=770  
ARG GID=770  
WORKDIR /tmp  
  
RUN addgroup -g $GID syncthing \  
&& adduser -s /bin/false -D -H -G syncthing -u $UID syncthing \  
&& apk add --no-cache \  
curl \  
shadow \  
su-exec \  
&& curl -L
https://github.com/syncthing/syncthing/releases/download/v$VERSION/syncthing-
linux-$ARCH-v$VERSION.tar.gz | tar zx \  
&& mkdir /app \  
&& mv syncthing-linux-$ARCH-v$VERSION/syncthing /app \  
&& chown -R syncthing:syncthing /app \  
&& chmod 750 -R /app \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
HEALTHCHECK \--interval=30s --retries=3 CMD curl --fail -H \"X-API-Key: $(cat
/root/.syncthing)\" http://127.0.0.1:8384/rest/system/ping || exit 1  
VOLUME /config /data  
EXPOSE 8384 22000 21027/UDP  
  
# disable upgrades  
ENV STNOUPGRADE=1  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["-home=/config", "-no-browser"]  

