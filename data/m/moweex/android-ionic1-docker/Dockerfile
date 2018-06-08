# Pull base image.  
FROM moweex/android-base  
  
# ——————————  
# Install Node and global packages  
# ——————————  
ENV NODE_VERSION 6.11.3  
RUN cd && \  
wget -q
http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
&& \  
tar -xzf node-v${NODE_VERSION}-linux-x64.tar.gz && \  
mv node-v${NODE_VERSION}-linux-x64 /opt/node && \  
rm node-v${NODE_VERSION}-linux-x64.tar.gz  
ENV PATH ${PATH}:/opt/node/bin  
# ——————————  
# Install Ionic & Cordova Frameworks  
# ——————————  
RUN npm install -g ionic@2.1.13  
RUN npm install -g cordova@6.5.0  
  
ENV LANG en_US.UTF-8

