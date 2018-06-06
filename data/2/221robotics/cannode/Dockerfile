FROM 221robotics/armv7hf-debian-qemu  
  
RUN [ "cross-build-start" ]  
  
# install apt packages  
RUN apt-get update && \  
apt-get install -y build-essential net-tools can-utils wget curl nano python
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# install node  
ENV NODE_VERSION 7.10.0  
RUN curl -SLO "http://resin-
packages.s3.amazonaws.com/node/v$NODE_VERSION/node-v$NODE_VERSION-linux-
armv7hf.tar.gz" \  
&& echo "bf81ad1ef8ecd6b261f1058f3bedefd0cd9be933d0068a91e87b00fa4afe4272
node-v7.10.0-linux-armv7hf.tar.gz" | sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-armv7hf.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-armv7hf.tar.gz" \  
&& npm config set unsafe-perm true -g --unsafe-perm \  
&& rm -rf /tmp/*  
  
# copy in scripts  
COPY ./entrypoint.sh /entrypoint.sh  
  
# make the scripts executable  
RUN chmod +x /entrypoint.sh  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
CMD [ "/entrypoint.sh" ]  
  
RUN [ "cross-build-end" ]  

