FROM golang:1.10.2  
LABEL maintainer="mlussier@gmail.com"  
  
# Env for apt-get  
ENV DEBIAN_FRONTEND noninteractive  
  
# ENV for Node and NPM  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 10.3.0  
#  
# gcc for cgo  
#  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
pkg-config \  
xz-utils\  
software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#  
# NodeJS  
# Origionaly taken from https://github.com/nodejs/docker-
node/blob/master/6.8/Dockerfile  
#  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
#  
# Install dep (latest)  
#  
RUN go get -u github.com/golang/dep/cmd/dep \  
#  
# Install VGO (experimental) see: https://github.com/golang/vgo  
&& go get -u golang.org/x/vgo \  
#  
# NPM Settings and global dependencies  
#  
&& /usr/local/bin/npm set progress=false \  
&& /usr/local/bin/npm config set loglevel warn \  
#  
# YARN Package Manager  
#  
&& npm install yarn prettier -g  

