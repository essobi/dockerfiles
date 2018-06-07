FROM alpine:3.5  
# add user and group first so their IDs don't change  
RUN addgroup node-red && adduser -G node-red -D -H node-red  
# su/sudo with proper signaling inside docker  
RUN apk add --no-cache su-exec  
  
# node.js and node-gyp  
ENV NODE_VERSION 6.9.2-r1  
ENV NODE_GYP_VERSION 3.5.0  
RUN set -xe \  
&& apk add --no-cache --virtual .nodejs-rundeps \  
curl \  
nodejs-lts@$NODE_VERSION \  
&& apk add --no-cache --virtual .node-gyp-deps \  
python \  
make \  
g++ \  
&& npm install -g node-gyp@$NODE_GYP_VERSION \  
&& rm -rf /tmp/npm-* /root/.npm  
  
ENV NODE_RED_VERSION 0.16.2  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
\  
&& curl -O -fSL "https://github.com/node-red/node-
red/releases/download/$NODE_RED_VERSION/node-red-$NODE_RED_VERSION.zip" \  
&& unzip -q node-red-$NODE_RED_VERSION.zip \  
&& rm node-red-$NODE_RED_VERSION.zip \  
&& mv /node-red-$NODE_RED_VERSION /node-red \  
&& cd node-red \  
&& npm install --production \  
\  
&& chmod +x red.js \  
&& ln -s /node-red/red.js /node-red/bin/node-red \  
\  
&& mkdir /data /config \  
&& cp settings.js /config/settings.js.dist \  
&& chown -R node-red:node-red /data /config \  
\  
&& rm -rf /tmp/npm-* /root/.npm \  
&& apk del .build-deps  
  
ENV PATH /node-red/bin:$PATH  
  
# make sure node-red is installing additional packages in /data  
ENV NPM_CONFIG_PREFIX /data  
ENV NPM_CONFIG_TMP /tmp/  
ENV NPM_CONFIG_CACHE /tmp/.npm  
  
VOLUME ["/data"]  
EXPOSE 1880  
  
HEALTHCHECK --interval=5s \--timeout=3s \--retries=3 \  
CMD curl --silent --fail --head http://localhost:1880/ || exit 1  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["node-red", "--settings", "/config/settings.js"]  

