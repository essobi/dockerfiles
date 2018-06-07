FROM alpine:3.6  
ARG UID=1000  
ARG GID=1000  
ENV APP_CONFIG=/data/config.js \  
BUILD_DEPS="make gcc g++"  
RUN addgroup -g ${GID} pushbullet \  
&& adduser -h /home/pushbullet -s /bin/bash -G pushbullet -u ${UID} -D
pushbullet \  
&& apk add --no-cache su-exec ca-certificates nodejs nodejs-npm python2
${BUILD_DEPS} \  
&& update-ca-certificates \  
&& mkdir -p /usr/src/app \  
&& mkdir -p /data  
  
WORKDIR /usr/src/app  
  
COPY .npmrc /usr/src/app/  
COPY package.json /usr/src/app/  
  
RUN npm set progress=false \  
&& npm install -g node-gyp \  
&& npm install -g --build-from-source level@3.0.0 \  
&& npm install \  
&& npm cache clean -f  
  
COPY . /usr/src/app/  
  
RUN mv /usr/src/app/docker-entrypoint.sh /usr/local/bin/ \  
&& mv /usr/src/app/config.docker.js /data/config.js \  
&& ./prune.sh \  
&& rm prune.sh \  
&& apk del --purge ${BUILD_DEPS} \  
&& chown -R pushbullet:pushbullet /usr/src/app \  
&& chown -R pushbullet:pushbullet /data  
  
VOLUME /data  
  
ENTRYPOINT [ "docker-entrypoint.sh" ]  
  
CMD [ "npm", "start", "--silent" ]  

