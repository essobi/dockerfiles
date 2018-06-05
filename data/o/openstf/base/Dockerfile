FROM ubuntu:14.04  
# Install app requirements. Trying to optimize push speed for dependant apps  
# by reducing layers as much as possible. Note that one of the final steps  
# installs development files for node-gyp so that npm install won't have to  
# wait for them on the first native module installation.  
RUN export DEBIAN_FRONTEND=noninteractive && \  
useradd --system \  
\--create-home \  
\--shell /usr/sbin/nologin \  
stf-build && \  
useradd --system \  
\--no-create-home \  
\--shell /usr/sbin/nologin \  
stf && \  
sed -i''
's@http://archive.ubuntu.com/ubuntu/@mirror://mirrors.ubuntu.com/mirrors.txt@'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y install wget && \  
cd /tmp && \  
wget --progress=dot:mega \  
https://nodejs.org/dist/v4.1.2/node-v4.1.2.tar.gz && \  
cd /tmp && \  
apt-get -y install python build-essential && \  
tar xzf node-v*.tar.gz && \  
rm node-v*.tar.gz && \  
cd node-v* && \  
export CXX="g++ -Wno-unused-local-typedefs" && \  
./configure && \  
make -j $(nproc) && \  
make install && \  
rm -rf /tmp/node-v* && \  
cd /tmp && \  
sudo -u stf-build -H /usr/local/lib/node_modules/npm/node_modules/node-
gyp/bin/node-gyp.js install && \  
apt-get -y install libzmq3-dev libprotobuf-dev git graphicsmagick yasm && \  
apt-get clean && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/*  

