FROM alpine  
MAINTAINER Nathan Douglas <docker@tenesm.us>  
  
ENV TR_RPC_PORT 9091  
ENV TR_LISTEN_PORT 51413  
ENV TR_RPC_USERNAME admin  
ENV TR_RPC_PASSWORD=  
  
RUN set -xe && \  
apk add \--no-cache transmission-daemon curl transmission-cli jq && \  
mkdir -p /config && \  
mkdir -p /downloads && \  
mkdir -p /incomplete && \  
mkdir -p /watch && \  
mkdir -p ~/.config/transmission-daemon && \  
ln -sf /config/settings.json ~/.config/transmission-daemon/settings.json  
  
COPY settings.json /config/settings.json  
  
VOLUME /config /downloads /incomplete /watch  
  
EXPOSE $TR_RPC_PORT $TR_LISTEN_PORT $TR_LISTEN_PORT/UDP  
  
CMD /usr/bin/transmission-daemon \  
\--allowed *.*.*.* \  
\--foreground \  
\--config-dir /config \  
\--port $TR_RPC_PORT \  
-c /watch \  
\--download-dir /downloads \  
\--incomplete-dir /incomplete \  
\--peerport $TR_LISTEN_PORT \  
\--username $TR_RPC_USERNAME \  
\--password ${TR_RPC_PASSWORD:-$(hostname)}  

