FROM frolvlad/alpine-glibc:latest  
  
MAINTAINER https://github.com/Pingoin/factorio_server_docker  
  
ARG USER=factorio  
ARG GROUP=factorio  
ARG PUID=1000  
ARG PGID=1000  
ENV PORT=34197 \  
RCON_PORT=27015 \  
VERSION=0.16.11 \  
ARGS="--start-server-load-latest --server-settings ./config/server-
settings.json"  
RUN mkdir -p /factorio && \  
apk add --update --no-cache pwgen && \  
apk add --update --no-cache --virtual .build-deps curl && \  
addgroup -g $PGID -S $GROUP && \  
adduser -u $PUID -G $USER -s /bin/sh -SDH $GROUP  
  
VOLUME /factorio  
  
EXPOSE $PORT/udp $RCON_PORT/tcp  
  
COPY ./docker-entrypoint.sh /  
  
RUN chown $USER:$GROUP /docker-entrypoint.sh &&\  
mkdir /factorio/config &&\  
mkdir /factorio/mods &&\  
mkdir /factorio/saves &&\  
chown -R $USER:$GROUP /factorio &&\  
chmod 777 /docker-entrypoint.sh  
  
USER $USER  
ENTRYPOINT /docker-entrypoint.sh $VERSION $ARGS  

