FROM alpine:3.4  
MAINTAINER Wonderlic DevOps <DevOps@wonderlic.com>  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.11.1  
  
RUN \  
apk add --no-cache \  
libstdc++ \  
libgcc \  
&& apk add --no-cache --virtual .build-deps \  
gnupg \  
curl \  
# gpg keys listed at https://github.com/nodejs/node#release-team  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -zxf "node-v$NODE_VERSION-linux-x64.tar.gz" "node-v$NODE_VERSION-
linux-x64/bin/node" \  
&& cp "node-v$NODE_VERSION-linux-x64/bin/node" /usr/bin/node \  
&& rm -Rf "node-v$NODE_VERSION-linux-x64" \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& apk del .build-deps  
  
CMD [ "node" ]  

