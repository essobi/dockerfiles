FROM google/debian:wheezy  
ARG NODE_MAJOR_VERSION=6  
# Based on https://github.com/sjevs/docker-node/  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git curl apt-transport-https lsb-
release ca-certificates && \  
  
# Installing node  
curl -sL https://deb.nodesource.com/setup_${NODE_MAJOR_VERSION}.x | bash - &&
\  
apt-get install -y nodejs && \  
  
apt-get purge --auto-remove -y curl libcurl3 python python-minimal python2.7
python2.7-minimal && \  
apt-get autoremove -y && \  
apt-get clean && \  
npm install -g yarn && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY package.json /usr/src/app/  
ONBUILD COPY yarn.lock /usr/src/app/  
ONBUILD RUN yarn install --production && /bin/rm -rf /tmp/npm* /root/.npm
/root/.node-gyp  
ONBUILD COPY . /usr/src/app  
  
CMD npm run start  

