FROM alpine:3.5  
MAINTAINER Ryan Schlesinger <ryan@outstand.com>  
  
# USAGE  
# $ docker build -t nfs-client .  
# $ docker run -it --privileged=true --net=host -v /mnt/nfs-1 -e
SERVER=192.168.0.9 -e SHARE=movies nfs-client  
# or detached:  
# $ docker run -itd --privileged=true --net=host -v /mnt/nfs-1 -e
SERVER=192.168.0.9 -e SHARE=movies nfs-client  
# or with some more options:  
# $ docker run -itd \  
# --name nfs-vols \  
# --restart=always \  
# --privileged=true \  
# --net=host \  
# -v /:/mnt/host \  
# -e SERVER=192.168.0.9 \  
# -e SHARE=movies \  
# -e MOUNT_OPTIONS="nfsvers=3,ro" \  
# -e FSTYPE=nfs \  
# -e MOUNTPOINT=/mnt/host \  
# nfs-client  
ENV DUMB_INIT_VERSION 1.2.0  
RUN apk add --no-cache curl ca-certificates && \  
mkdir -p /tmp/build && \  
cd /tmp/build && \  
curl -O -L https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 && \  
curl -O -L https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/sha256sums && \  
grep dumb-init_${DUMB_INIT_VERSION}_amd64$ sha256sums | sha256sum -c && \  
chmod +x dumb-init_${DUMB_INIT_VERSION}_amd64 && \  
cp dumb-init_${DUMB_INIT_VERSION}_amd64 /bin/dumb-init && \  
ln -s /bin/dumb-init /usr/bin/dumb-init && \  
cd /tmp && \  
rm -rf /tmp/build && \  
apk del curl  
  
ENV FSTYPE nfs4  
ENV MOUNT_OPTIONS nfsvers=4  
ENV MOUNTPOINT /mnt/nfs-1  
RUN apk add --no-cache --update nfs-utils && \  
rm /sbin/halt /sbin/poweroff /sbin/reboot  
  
HEALTHCHECK \--interval=1s --timeout=5s --start-period=60s \  
CMD mount -t "$FSTYPE" | grep "$SERVER:$SHARE" || exit 1  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

