FROM rickydunlop/nodejs-ffmpeg:latest  
  
LABEL maintainer frosty5689 <frosty5689@gmail.com>  
  
RUN apk add --no-cache --update \  
ca-certificates \  
tzdata \  
dumb-init \  
&& update-ca-certificates  
  
ARG MPEGTS_PROXY_VERSION=master  
  
EXPOSE 80  
ENV PORT=80  
RUN apk add --no-cache --update --virtual build-dependencies make g++ python
wget unzip && \  
wget -O /tmp/mpegts-proxy-$MPEGTS_PROXY_VERSION.zip
https://github.com/Jalle19/node-ffmpeg-mpegts-
proxy/archive/$MPEGTS_PROXY_VERSION.zip && \  
ls -l /tmp && \  
mkdir -p /opt && \  
unzip /tmp/mpegts-proxy-$MPEGTS_PROXY_VERSION.zip -d /opt && \  
mv /opt/node-ffmpeg-mpegts-proxy* /opt/node-ffmpeg-mpegts-proxy && \  
cd /opt/node-ffmpeg-mpegts-proxy && \  
npm install && \  
rm -rf /tmp/mpegts-proxy-$HATH_VERSION.zip && \  
apk del build-dependencies  
  
ADD run/* /opt/node-ffmpeg-mpegts-proxy/  
  
VOLUME /config  
  
WORKDIR /opt/node-ffmpeg-mpegts-proxy  
  
CMD ["/opt/node-ffmpeg-mpegts-proxy/start.sh"]  

