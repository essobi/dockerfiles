# Version 1.0.1  
  
FROM nothingdocker/centos-systemd  
ENV NODE_VER v8.2.1  
RUN cd /usr/local;\  
wget https://nodejs.org/dist/$NODE_VER/node-$NODE_VER-linux-x64.tar.xz;\  
tar xJf node-$NODE_VER-linux-x64.tar.xz;\  
rm -f node.tar.xz;\  
mv node-$NODE_VER-linux-x64 node;\  
ln -s /usr/local/node/bin/node /usr/local/bin/node;\  
ln -s /usr/local/node/bin/npm /usr/local/bin/npm  
RUN echo "PATH=/usr/local/node/bin:$PATH" >> /etc/bashrc; \  
echo "export PATH" >> /etc/bashrc;  
RUN echo "alias cnpm=\"npm --registry=https://registry.npm.taobao.org \  
\--cache=$HOME/.npm/.cache/cnpm \  
\--disturl=https://npm.taobao.org/dist \  
\--userconfig=$HOME/.cnpmrc\"" >> /etc/bashrc;  
  
#RUN npm install -g node-gyp  

