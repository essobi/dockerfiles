# docker build --tag gdnsd --build-arg GDNS_VER=2.2.4 .  
FROM alpine:3.6  
MAINTAINER Baptiste Assmann <bedis9@gmail.com>  
  
ARG GDNS_VER=  
  
ENV GDNS_OPT="--prefix=/ --datarootdir=/usr" GDNS_BUILD_DEPENDENCY="libev perl
perl-libwww ragel libev libev-dev"  
ENV DEL_PKGS="libev-dev gcc g++ patch file openssl" RM_DIRS="/usr/src/*
/var/cache/apk/*"  
ADD 0001-WIP-stats-page-URL-change.patch /usr/src/gdnsd-${GDNS_VER}/  
  
RUN apk update \  
&& apk add gcc g++ make patch file openssl ${GDNS_BUILD_DEPENDENCY} \  
&& addgroup -S -g 101 gdnsd \  
&& adduser -S -H -D -u 100 -s /sbin/nologin gdnsd gdnsd \  
&& cd /usr/src \  
&& wget
https://github.com/gdnsd/gdnsd/releases/download/v${GDNS_VER}/gdnsd-${GDNS_VER}.tar.xz
\  
&& tar xJf gdnsd-${GDNS_VER}.tar.xz \  
&& cd gdnsd-${GDNS_VER} \  
&& patch -p 1 <0001-WIP-stats-page-URL-change.patch \  
&& ./configure ${GDNS_OPT} \  
&& make \  
&& make install \  
&& apk del ${DEL_PKGS} \  
&& rm -rf ${RM_DIRS}  
  
ENTRYPOINT [ "/sbin/gdnsd", "-f", "start" ]  

