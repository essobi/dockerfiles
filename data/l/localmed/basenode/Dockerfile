FROM localmed/baseimage:1.1  
MAINTAINER LocalMed <developers@localmed.com>  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 5.6.0  
RUN wget -q "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz"  

