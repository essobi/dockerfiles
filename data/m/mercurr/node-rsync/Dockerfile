FROM node:8.9.4  
  
RUN apt-get clean && \  
apt-get update && \  
apt-get -y install rsync  
  
RUN rm -rf /usr/local/lib/node_modules/npm \  
&& mkdir /usr/local/lib/node_modules/npm \  
&& curl -sL https://github.com/npm/npm/archive/v5.7.1.tar.gz | tar xz -C
/usr/local/lib/node_modules/npm \--strip-components=1 \  

