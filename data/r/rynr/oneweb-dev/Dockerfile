FROM node:4.5.0  
  
LABEL version.npm=3.10.6  
LABEL version.sass=3.8.0  
LABEL version.phantomjs=2.1.7  
  
RUN npm install -g npm@3.10.6 \  
&& npm install -g node-gyp-install \  
&& node-gyp-install \  
&& npm install -g node-sass@3.8.0 \  
&& npm install -g phantomjs-prebuilt@2.1.7 \  
&& chmod -R a+w `npm root -g` \  
&& mkdir -p /opt/ci && chmod 777 /opt/ci \  
&& rm -rf /var/lib/apt/lists/* /tmp/npm-*  
  
WORKDIR /opt/ci  

