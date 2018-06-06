FROM alpine:3.5  
MAINTAINER cola <colachg@gmail.com>  
  
ARG KCP_VER=20170904  
ARG
KCP_URL=https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-
linux-amd64-$KCP_VER.tar.gz  
  
WORKDIR /kcptun  
  
RUN set -ex &&\  
apk add --no-cache --virtual .build curl &&\  
curl -sSL $KCP_URL | tar xz -C /usr/local/bin/ &&\  
apk del --purge .build &&\  
rm -rf /var/cache/* /tmp/*  
  
WORKDIR /kcptun  
  
EXPOSE 4000/udp  
  
CMD server_linux_amd64 -c kcptun.json  

