FROM alpine:latest  
LABEL MAINTAINER "Eric Weissgerber <eweissge@gmail.com>"  
  
# These ENV variables may not be needed as settings file is intact  
ENV LOCAL_NETWORK=192.168.1.0/24  
ENV RPC_PORT 9091  
ENV PEERPORT 51413  
ENV USERNAME eric  
ENV PASSWORD={9db599fdd7350579165e0b2275bb80a69c76a68fGBY9jz.R  
  
# Let's roll  
RUN set -xe && \  
apk add --no-cache transmission-daemon tar curl && \  
  
cd /tmp && \  
curl -sSL https://raw.githubusercontent.com/ronggang/transmission-web-
control/master/release/transmission-control-full.tar.gz | tar xz && \  
  
cp /usr/share/transmission/web/index.html
/usr/share/transmission/web/index.original.html && \  
cp -r /tmp/web /usr/share/transmission/ && \  
  
apk del tar curl && \  
rm -rf /tmp/*  
  
COPY settings.json /etc/transmission/settings.json  
  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
# No destination volume mapping?  
#VOLUME /data  
VOLUME /data/downloads  
VOLUME /data/incomplete  
  
# Settings file opens random port, may need to switch to static for this  
EXPOSE $RPC_PORT $PEERPORT $PEERPORT/UDP  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
# May not need these extra args, needs testing  
CMD /usr/bin/transmission-daemon \  
\--foreground \  
\--config-dir /data/.config \  
\--port $RPC_PORT \  
\--peerport $PEERPORT \  
\--username $USERNAME \  
\--password ${PASSWORD:-$(hostname)}  

