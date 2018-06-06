FROM alljoynsville/android  
  
MAINTAINER alljoynsville  
  
RUN nodeVersion=node-v5.3.0-linux-x64 && \  
wget -qO- https://nodejs.org/dist/latest/$nodeVersion.tar.gz | tar -zx -C
/usr/local/ && \  
ln -s /usr/local/$nodeVersion/bin/node /usr/bin/node && \  
ln -s /usr/local/$nodeVersion/bin/npm /usr/bin/npm  
  
RUN nodeVersion=node-v5.3.0-linux-x64 && \  
npm install -g cordova && \  
ln -s /usr/local/$nodeVersion/lib/node_modules/cordova/bin/cordova
/usr/bin/cordova  
  

