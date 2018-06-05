FROM alpine:edge  
  
RUN set -x &&\  
apk add --no-cache --upgrade alpine-sdk &&\  
adduser -D skilld &&\  
echo "skilld ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers &&\  
addgroup skilld abuild &&\  
mkdir -p /var/cache/distfiles &&\  
chmod a+w /var/cache/distfiles &&\  
chgrp abuild /var/cache/distfiles &&\  
chmod g+w /var/cache/distfiles &&\  
sudo -u skilld abuild-keygen -a -i -n  
  
VOLUME /mnt  
WORKDIR /mnt  
USER skilld  
CMD ["ash"]

