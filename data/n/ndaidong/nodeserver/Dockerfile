FROM ndaidong/ubuntu  
  
MAINTAINER @ndaidong  
  
ENV NODE_VERSION 8.11.1  
ENV NODE_DOWNLOAD_URL
https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz  
  
RUN export LANG=C.UTF-8 && \  
apt update --fix-missing && apt upgrade -y && \  
apt install --no-install-recommends -y \  
git python gcc g++ && \  
cd /home && \  
wget "$NODE_DOWNLOAD_URL" -O node-v$NODE_VERSION.tar.gz && \  
tar -zxvf node-v$NODE_VERSION.tar.gz && \  
cd node-v$NODE_VERSION && \  
./configure && \  
make && \  
make install && \  
npm i -g npm && \  
node -v && \  
npm -v && \  
cd /home && \  
rm -rf node-v$NODE_VERSION && \  
rm node-v$NODE_VERSION.tar.gz && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /home  

