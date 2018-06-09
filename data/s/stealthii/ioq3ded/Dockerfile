FROM alpine:3.3  
  
MAINTAINER Dan Porter "dpreid@gmail.com"  
  
RUN \  
addgroup -S quake3 \  
&& adduser -D -S -h /var/cache/quake3 -s /sbin/nologin -G quake3 quake3 \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
curl \  
&& curl -fSL https://github.com/ioquake/ioq3/archive/master.zip -o quake3.zip
\  
&& mkdir -p /usr/src \  
&& unzip quake3.zip -d /usr/src \  
&& rm quake3.zip \  
&& cd /usr/src/ioq3-master \  
&& BUILD_CLIENT=0 make copyfiles \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/local/games/quake3
/usr/local/games/quake3/baseq3/*.so \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .quake3-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/ioq3-master \  
&& apk add --no-cache gettext  
  
ENV PATH /usr/local/games/quake3:$PATH  
  
EXPOSE 27960 27960/udp  
  
CMD ["ioq3ded.x86_64"]  

