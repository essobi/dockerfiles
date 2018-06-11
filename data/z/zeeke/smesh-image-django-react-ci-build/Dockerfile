FROM ubuntu:16.04  
RUN \  
apt-get update -qq && \  
apt-get install -y \  
git \  
libffi-dev \  
python2.7 \  
python-pip \  
curl \  
libssl-dev \  
libpq-dev  
  
ENV NODE_VERSION 6.9.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  

