FROM maxird/centos:7  
  
RUN export VERSION=8.11.2 && \  
cd /opt && \  
wget -q https://nodejs.org/dist/v${VERSION}/node-v${VERSION}-linux-x64.tar.xz
&& \  
tar xf node-v${VERSION}-linux-x64.tar.xz && \  
mv node-v${VERSION}-linux-x64 node && \  
chown -R root:root node && \  
rm node-v${VERSION}-linux-x64.tar.xz && \  
export PATH=/opt/node/bin:$PATH && \  
npm config set user 0 && \  
npm config set unsafe-perm true && \  
npm -g upgrade npm --log-level=warn && \  
npm -g install node-gyp nan && \  
npm -g install nodemon --production --log-level=warn && \  
npm -g install bunyan --production --log-level=warn && \  
npm -g install nsp --production --log-level=warn && \  
npm -g install auditjs --production --log-level=warn && \  
chown -R root:root node && \  
rm -rf ~/.npm && \  
alternatives --install /usr/bin/node node /opt/node/bin/node 0 && \  
alternatives --install /usr/bin/npm npm /opt/node/bin/npm 0 && \  
alternatives --install /usr/bin/nodemon nodemon /opt/node/bin/nodemon 0 && \  
alternatives --install /usr/bin/bunyan bunyan /opt/node/bin/bunyan 0 && \  
alternatives --install /usr/bin/nsp nsp /opt/node/bin/nsp 0 && \  
echo 'export PATH=/opt/node/bin:$PATH' > /etc/profile.d/node.sh  

