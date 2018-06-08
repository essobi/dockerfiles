FROM buildpack-deps:xenial  
# official node images are debian based and `bf` is not available.  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
# Install NodeJS from [NodeSource Node.js Binary
Distributions](https://github.com/nodesource/distributions)  
RUN set -ex; \  
curl -sL https://deb.nodesource.com/setup_8.x | bash -; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
# bf (20041219ubuntu5)  
bf \  
nodejs \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
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

