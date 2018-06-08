FROM node:8.11.1-alpine  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apk add \--no-cache \  
sqlite-libs \  
# for node-canvas  
bash \  
build-base \  
cairo-dev \  
jpeg-dev \  
pango-dev \  
giflib-dev \  
# installing some fonts  
ttf-dejavu \  
;  
  
ENV NPM_CONFIG_LOGLEVEL=warn NODE_ENV=production  
COPY rootfs/opt/cw-2 /opt/cw-2  
COPY rootfs/runner/package.json /runner/package.json  
COPY rootfs/runner/yarn.lock /runner/yarn.lock  
RUN cd /runner && yarn install --frozen-lockfile  
  
WORKDIR /workspace  
  
COPY rootfs/runner/frameworks /runner/frameworks  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
PATH=/runner/node_modules/.bin:$PATH \  
NODE_PATH=/runner/node_modules:/usr/lib/node_modules  

