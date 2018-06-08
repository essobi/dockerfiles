FROM node:alpine  
  
ARG MEDIAINFO_VERSION=0.7.99  
ARG FLOOD_VERSION=v1.0.0  
  
RUN addgroup -S flood \  
&& adduser -S -G flood -s /bin/sh -h /var/lib/flood flood \  
&& apk add --no-cache --update --virtual .build-deps \  
git \  
bzip2 \  
wget \  
autoconf \  
automake \  
build-base \  
zlib-dev \  
&& cd /tmp \  
&& wget
https://mediaarea.net/download/binary/mediainfo/${MEDIAINFO_VERSION}/MediaInfo_CLI_${MEDIAINFO_VERSION}_GNU_FromSource.tar.bz2
\  
&& tar -xjf MediaInfo_CLI_${MEDIAINFO_VERSION}_GNU_FromSource.tar.bz2 \  
&& cd MediaInfo_CLI_GNU_FromSource \  
&& sh ./CLI_Compile.sh --build=x86_64-alpine-linux-musl --host=x86_64-alpine-
linux-musl \  
&& cd MediaInfo/Project/GNU/CLI \  
&& make install \  
&& cd /var/lib/flood \  
&& git clone -b ${FLOOD_VERSION} https://github.com/jfurrow/flood.git . \  
&& npm install --production \  
&& npm cache clean --force \  
&& cp config.docker.js config.js \  
&& chown -R flood: /var/lib/flood \  
&& mkdir /data \  
&& chown -R flood: /data \  
&& rm -rf /tmp/* \  
&& apk del .build-deps  
  
EXPOSE 3000  
  
WORKDIR /var/lib/flood  
  
USER flood  
  
CMD [ "npm", "start", "--production", "/var/lib/flood" ]

