# VERSION 0.1  
# DOCKER-VERSION 1.6.0  
# Base container  
FROM ubuntu:14.04  
# Author  
MAINTAINER "Vijay Harrell" <vijay@wolfpackdigital.com>  
  
# Install ifconfig and other utilities  
RUN apt-get update && apt-get install -y \  
net-tools \  
vim \  
aufs-tools \  
automake \  
btrfs-tools \  
build-essential \  
curl \  
dpkg-sig \  
git \  
iptables \  
libapparmor-dev \  
libcap-dev \  
libsqlite3-dev \  
lxc=1.0* \  
mercurial \  
parallel \  
reprepro \  
ruby1.9.1 \  
ruby1.9.1-dev \  
s3cmd=1.1.0*  
  
# Install Node.js  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.30/SHASUMS256.txt.asc  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
ENV NODE_VERSION 0.12.2  
ENV NPM_VERSION 2.7.3  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
# App  
ADD . /src  
RUN chmod 777 -R /src  
  
# Install app dependencies  
WORKDIR /src  
RUN npm install -g forever forever-monitor && npm install  
RUN touch .foreverignore  
  
# Expose PORTS  
EXPOSE 3000  
CMD [ "sh", "-c", "/src/start.sh" ]

