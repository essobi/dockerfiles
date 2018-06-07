FROM jenkinsci/jnlp-slave  
  
MAINTAINER Linki <vilasmaciel@gmail.com>  
USER root  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV DOCKER_VERSION 1.12.6  
ENV NODE_VERSION 7.10.0  
ENV COMPOSE_VERSION 1.12.0  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
&& npm install -g yarn  
  
RUN apt-get update && apt-get install -y git jq rsync g++ build-essential &&
apt-get clean  
  
# Install Docker binary  
RUN curl -fsSLO
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && tar
--strip-components=1 -xvzf docker-${DOCKER_VERSION}.tgz -C /usr/bin  
  
# Install wine  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && dpkg --add-architecture i386 && apt-get update  
RUN apt-get install -y wine/jessie-backports \  
wine32/jessie-backports \  
wine64/jessie-backports \  
libwine/jessie-backports \  
libwine:i386/jessie-backports \  
fonts-wine/jessie-backports  
  
# Install Mono  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && echo "deb http://download.mono-
project.com/repo/debian jessie main" | tee /etc/apt/sources.list.d/mono-
official.list && apt-get update  
RUN apt-get install -y mono-devel  
  
# Clean caches  
RUN apt-get clean && npm cache clean  
  
ADD wait-for-it /usr/local/bin

