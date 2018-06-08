# web  
FROM pitchplay/scala-dev:jdk8  
MAINTAINER Evan Lowry <evan@pitchplay.io>  
  
# Install Node  
ENV NODE_VERSION 0.12.5  
ENV NPM_VERSION 2.11.3  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
# Setup code location  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["/usr/bin/sbt"]  
CMD ["-h"]  

