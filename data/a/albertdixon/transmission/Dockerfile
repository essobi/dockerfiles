FROM alpine:3.5  
MAINTAINER Albert Dixon <albert.dixon@schange.com>  
  
ENTRYPOINT ["/sbin/tini", "-g","--", "/sbin/entry"]  
CMD ["/sbin/start"]  
EXPOSE 9091  
  
ENV T2_VER=v2.2.1 \  
TRANSMON_VER=v0.2.3  
  
WORKDIR /  
RUN apk add --update --no-cache \  
bash \  
ca-certificates \  
curl \  
openvpn \  
tar \  
tini \  
transmission-daemon \  
unzip \  
&& mkdir -vp \  
/certs \  
/etc/pia_transmission_monitor \  
/openvpn \  
/transmission/openvpn \  
/web \  
&& curl -L -o t2.tgz
https://github.com/albertrdixon/tmplnator/releases/download/${T2_VER}/t2-linux.tgz
\  
&& curl -L -o transmon.tgz
https://github.com/albertrdixon/transmon/releases/download/${TRANSMON_VER}/transmon-
linux.tgz \  
&& curl -L -o web.tgz https://github.com/balonik/transmission-web-
control/raw/master/release/transmission-control-full.tar.gz \  
&& curl -kL -o openvpn.zip
https://www.privateinternetaccess.com/openvpn/openvpn.zip \  
&& tar xvzf /t2.tgz -C /bin \  
&& tar xvzf /transmon.tgz -C /bin \  
&& tar xvzf /web.tgz -C /web \  
&& unzip -Lj /openvpn.zip ca.*.crt crl.*.pem -d /openvpn \  
&& mv -vf /openvpn/ca.*.crt /certs/pia.crt \  
&& mv -vf /openvpn/crl.*.pem /certs/pia.pem \  
&& deluser transmission \  
&& rm -rvf /openvpn* /*.tgz  
  
COPY bashrc /root/.bashrc  
COPY configs /templates  
  
COPY scripts/completed.sh /scripts/completed.sh  
COPY ["scripts/entry", "scripts/start", "/sbin/"]  
RUN chmod +rx /sbin/entry /sbin/start /scripts/completed.sh  
  
ENV CACHE_SIZE=50 \  
CLEANER_ENABLED=true \  
COMPLETED_SCRIPT=/scripts/completed.sh \  
COMPLETED_SCRIPT_ENABLED=false \  
CONGESTION=lp \  
DOWNLOAD_DIR=/downloads \  
DOWNLOAD_QUEUE_ENABLED=true \  
DOWNLOAD_QUEUE_SIZE=3 \  
IDLE_SEEDING_LIMIT=10 \  
MESSAGE_LEVEL=1 \  
OPEN_FILE_LIMIT=32768 \  
OPENVPN_GATEWAY=ca-toronto.privateinternetaccess.com \  
OPENVPN_GATEWAY_PORT=1198 \  
OPENVPN_HOME=/transmission/openvpn \  
OPENVPN_LOG=/dev/stderr \  
OPENVPN_MUTE=20 \  
OPENVPN_PROTO=udp \  
OPENVPN_VERB=3 \  
PATH=/usr/local/bin:$PATH \  
PEER_LIMIT_GLOBAL=1200 \  
PEER_LIMIT_PER_TORRENT=180 \  
PEER_PORT=51234 \  
QUEUE_STALLED_ENABLED=true \  
QUEUE_STALLED_MINUTES=5 \  
RATIO_LIMIT=1 \  
RATIO_LIMIT_ENABLED=true \  
RPC_AUTHENTICATION_REQUIRED=false \  
RPC_PASSWORD=client \  
RPC_PORT=9091 \  
RPC_USERNAME=client \  
SEED_QUEUE_ENABLED=true \  
SEED_QUEUE_SIZE=2 \  
SPEED_LIMIT_DOWN=5000 \  
SPEED_LIMIT_DOWN_ENABLED=false \  
SPEED_LIMIT_UP=400 \  
SPEED_LIMIT_UP_ENABLED=true \  
SUPERVISOR_LOG_LEVEL=INFO \  
TRANSMISSION_HOME=/transmission \  
TRANSMISSION_LOG_LEVEL=info \  
TRANSMISSION_WEB_HOME=/web \  
TRANSMISSION_UID=7000 \  
TRANSMISSION_GID=7000 \  
TRANSMON_LOG_LEVEL=info \  
UPLOAD_SLOTS_PER_TORRENT=14 \  
WATCH_DIR=/torrents \  
WATCH_DIR_ENABLED=false  

