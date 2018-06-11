FROM ubuntu:16.04  
  
RUN apt-get update -qq && \  
apt-get install wget git nginx -yqq && \  
wget -cq https://nodejs.org/dist/v6.10.3/node-v6.10.3-linux-x64.tar.gz && \  
\  
tar -zxf node-v6.10.3-linux-x64.tar.gz && \  
rm -rf /node-v6.10.3-linux-x64.tar.gz && \  
# apt-get purge wget -y && \  
\  
mv node-v6.10.3-linux-x64 /usr/local/src/node && \  
cd /usr/local/src/node && \  
# cp -R lib/* /usr/local/lib && \  
cp -R share/* /usr/local/share && \  
ln -s /usr/local/src/node/bin/node /usr/local/bin/node && \  
ln -s /usr/local/src/node/bin/npm /usr/local/bin/npm && \  
\  
# rm -rf /usr/local/src/node/lib && \  
rm -rf /usr/local/src/node/share && \  
rm -rf /usr/local/src/node/include && \  
rm -rf /usr/local/src/node/CHANGELOG.md && \  
rm -rf /usr/local/src/node/LICENSE && \  
rm -rf /usr/local/src/node/README.md && \  
\  
# delete cache and tmp files  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/cache/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
\  
# set npm config  
npm config set depth 0 && \  
\  
# change dir  
cd /  

