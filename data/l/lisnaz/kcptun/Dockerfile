#  
# Dockerfile for kcptun  
#  
FROM alpine  
MAINTAINER Vincent.Gu <v@vgu.io>  
  
ENV KCPTUN_VER 20180305  
ENV KCPTUN_KEY password  
ENV KCPTUN_CRYPT aes  
ENV KCPTUN_MODE fast2  
ENV KCPTUN_CONN 2  
ENV KCPTUN_AUTO_EXPIRE 0  
ENV KCPTUN_MTU 1200  
ENV KCPTUN_SNDWND 1024  
ENV KCPTUN_RCVWND 1024  
ENV KCPTUN_DATASHARD 10  
ENV KCPTUN_PARITYSHARD 3  
ENV KCPTUN_DSCP 46  
ENV KCPTUN_NOCOMP true  
ENV KCPTUN_LOG /dev/stderr  
  
# define default directory  
ENV APP_DIR /srv/kcptun  
WORKDIR $APP_DIR  
  
# build kcptun  
ENV KCPTUN_URL
https://github.com/xtaci/kcptun/releases/download/v${KCPTUN_VER}/kcptun-linux-
amd64-${KCPTUN_VER}.tar.gz  
ENV KCPTUN_TDEP curl  
RUN set -ex \  
&& apk add --update $KCPTUN_TDEP \  
&& curl -sSL $KCPTUN_URL | tar xz \  
&& apk del --purge $KCPTUN_TDEP \  
&& rm -rf /var/cache/apk/*  

