FROM frolvlad/alpine-glibc:alpine-3.6  
  
MAINTAINER Jessica Smith <jess@mintopia.net>  
  
ARG USER=factorio  
ARG GROUP=factorio  
ARG PUID=845  
ARG PGID=845  
  
ENV PORT=34197 \  
RCON_PORT=27015 \  
VERSION=0.16.47  
  
VOLUME /factorio  
  
COPY ./docker-entrypoint.sh /  
  
RUN mkdir -p /opt && \  
apk add --update --no-cache pwgen && \  
apk add --update --no-cache --virtual .build-deps curl && \  
curl -sSL https://www.factorio.com/get-download/$VERSION/headless/linux64 \  
-o /tmp/factorio_headless_x64_$VERSION.tar.xz && \  
tar xf /tmp/factorio_headless_x64_$VERSION.tar.xz \--directory /opt && \  
chmod ugo=rwx /opt/factorio && \  
rm /tmp/factorio_headless_x64_$VERSION.tar.xz && \  
ln -s /factorio/saves /opt/factorio/saves && \  
ln -s /factorio/mods /opt/factorio/mods && \  
apk del .build-deps && \  
addgroup -g $PGID -S $GROUP && \  
adduser -u $PUID -G $USER -s /bin/sh -SDH $GROUP && \  
chmod +x docker-entrypoint.sh && \  
chown -R $USER:$GROUP /opt/factorio /factorio  
  
EXPOSE $PORT/udp $RCON_PORT/tcp  
  
USER $USER  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

