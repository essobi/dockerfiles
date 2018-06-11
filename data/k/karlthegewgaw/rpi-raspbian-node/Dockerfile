FROM karlthegewgaw/rpi-raspbian-userland:test  
  
RUN [ "cross-build-start" ]  
  
ENV NODE_VERSION 7.5.0  
RUN apt-get update && apt-get install -y curl \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-armv7l.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-armv7l.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-armv7l.tar.gz" \  
&& rm -rf /tmp/*  
  
CMD npm config set unsafe-perm true -g --unsafe-perm && npm start  
  
RUN [ "cross-build-end" ]  

