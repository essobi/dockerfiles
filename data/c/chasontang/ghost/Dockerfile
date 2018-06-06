FROM chasontang/node:4.4.7  
MAINTAINER ChasonTang <chasontang@gmail.com>  
  
ENV GOSU_VERSION 1.7  
ENV GHOST_VERSION 0.9.0  
ENV GHOST_SOURCE /usr/src/ghost  
ENV GHOST_CONTENT /var/lib/ghost  
ENV NODE_ENV production  
  
WORKDIR $GHOST_SOURCE  
  
RUN apk add --no-cache openssl tar \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& addgroup -S ghost \  
&& adduser -h $GHOST_SOURCE -S -G ghost -s /bin/sh ghost \  
&& wget -O ghost.zip "https://ghost.org/archives/ghost-${GHOST_VERSION}.zip" \  
&& unzip ghost.zip \  
&& npm install --production \  
&& rm ghost.zip \  
&& npm cache clean \  
&& rm -rf /tmp/npm* \  
&& mkdir -p "$GHOST_CONTENT" \  
&& chown -R ghost:ghost "$GHOST_CONTENT"  
  
VOLUME $GHOST_CONTENT  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 2368  
CMD ["node", "index"]

