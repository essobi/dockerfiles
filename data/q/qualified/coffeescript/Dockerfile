FROM node:8.7.0-alpine  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
ENV NPM_CONFIG_LOGLEVEL=warn NODE_ENV=production  
COPY rootfs/runner/package.json /runner/package.json  
RUN cd /runner && npm install  
  
WORKDIR /workspace  
  
COPY rootfs/runner/frameworks /runner/frameworks  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
PATH=/runner/node_modules/.bin:$PATH \  
NODE_PATH=/runner/node_modules:/usr/lib/node_modules  

