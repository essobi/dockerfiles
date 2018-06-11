FROM java:8  
#Install maven  
RUN apt-get update  
RUN apt-get install -y maven  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.3.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
WORKDIR /build  
  
# Dependencies  
ADD pom.xml /build/pom.xml  
ADD package.json /build/package.json  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
RUN ["npm", "install"]  
  
# Compile and package jar  
ADD src /build/src  
RUN ["mvn", "package"]  
  
#Setup Config  
ENV MSG_NODE_CONFIG dev  
ADD node.config.json /build/node.config.json  
ADD server-keystore.jks /build/server-keystore.jks  
ADD policy.json /build/policy.json  
  
#Run msg-node  
EXPOSE 9090  
CMD ["mvn", "exec:java"]  

