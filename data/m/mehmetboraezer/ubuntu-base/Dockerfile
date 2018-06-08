FROM ubuntu:14.04  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
useradd --system \  
\--create-home \  
\--shell /usr/sbin/nologin \  
interactive-build && \  
useradd --system \  
\--no-create-home \  
\--shell /usr/sbin/nologin \  
interactive && \  
apt-get update && \  
apt-get -y install wget && \  
cd /tmp && \  
wget --progress=dot:mega \  
https://nodejs.org/dist/v0.12.7/node-v0.12.7.tar.gz && \  
cd /tmp && \  
apt-get -y install python build-essential ninja-build && \  
tar xzf node-v*.tar.gz && \  
rm node-v*.tar.gz && \  
cd node-v* && \  
export CXX="g++ -Wno-unused-local-typedefs" && \  
./configure --ninja && \  
make && \  
make install && \  
rm -rf /tmp/node-v* && \  
cd /tmp && \  
sudo -u interactive-build -H
/usr/local/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js install
&& \  
apt-get -y install libzmq3-dev libprotobuf-dev git graphicsmagick && \  
apt-get clean && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/*  

