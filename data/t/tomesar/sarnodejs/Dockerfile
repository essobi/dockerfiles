FROM tomesar/armv7hf-debian-qemu  
  
RUN [ "cross-build-start" ]  
  
# install curl/build-essential/https apt  
RUN apt-get update && apt-get install -y curl build-essential apt-transport-
https python-dev git  
  
# setup yarn apt repo  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# install yarn and cleanup  
RUN apt-get update && \  
apt-get install -y yarn && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# install node  
ENV NODE_VERSION 7.8.0  
RUN curl -SLO "http://resin-
packages.s3.amazonaws.com/node/v$NODE_VERSION/node-v$NODE_VERSION-linux-
armv7hf.tar.gz" \  
&& echo "3a1297d70adca2916ff28c45b68345b02ac1e419dffa3cfe7891805e731f57b0
node-v7.8.0-linux-armv7hf.tar.gz" | sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-armv7hf.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-armv7hf.tar.gz" \  
&& npm config set unsafe-perm true -g --unsafe-perm \  
&& rm -rf /tmp/*  
  
CMD ["echo","'No CMD command was set in Dockerfile!"]  
  
RUN [ "cross-build-end" ]  

