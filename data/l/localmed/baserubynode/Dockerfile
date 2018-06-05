FROM localmed/baseruby:1.2  
MAINTAINER LocalMed <developers@localmed.com>  
  
ENV NODE_VERSION 0.12.5  
ENV NPM_VERSION 2.12.1  
RUN wget -q "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  

