###  
# LaVue  
#  
# Repository: Alpine  
# Image:  
# Base distro: Alpine 3.7  
#  
FROM alpine:3.7  
LABEL description="Base Alpine image used in other containers"  
LABEL maintainer="4ngo.ru@gmail.com"  
  
ENV TIMEZONE=${TIMEZONE:-Europe/Kiev} \  
TERM=xterm-256color \  
COLORTERM=truecolor  
  
# Add the script to set TIMEZONE  
COPY settz.sh /usr/local/bin/settz  
  
# ToDo: COPY bashrc /home/lavue/.bashrc  
RUN set -xe \  
&& chmod +x /usr/local/bin/settz \  
&& apk add --update --no-cache \  
tini \  
bash \  
ca-certificates \  
curl \  
gzip \  
tar \  
unzip \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data \  
&& adduser -D -u 1000 -s /bin/bash lavue \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/* \  
&& settz  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
LABEL version="0.4.5-3.7"  

