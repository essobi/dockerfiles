FROM winworks/winworksone-base:2.3.3  
  
ENV PATH /usr/local/node/bin:$PATH  
  
RUN NODE_VERSION=4.3.2 \  
# Bower: git  
# Gemfile-git: git  
# mysql2: libmysqlclient-dev make  
# nokogiri: gcc make patch  
# passenger: g++ make  
# passenger-config install-standalone-runtime: wget  
# unf_ext: g++ make  
&& buildDeps=' \  
g++ \  
git \  
libmysqlclient-dev \  
make \  
patch \  
wget \  
' \  
\  
# apt  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -r /var/lib/apt/lists/* \  
\  
# Node.js  
&& mkdir /usr/local/node \  
&& wget https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz -O - \  
| tar -xz -C /usr/local/node \--strip-components 1 \  
\  
# Bower  
&& npm install -g bower  

