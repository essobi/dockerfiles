FROM ubuntu  
MAINTAINER Rafael de Morais "rdemorais.freitas@gmail.com"  
RUN apt-get update && \  
apt-get install -y curl \--no-install-recommends && \  
curl -k -L https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
apt-get install -y git \--no-install-recommends && \  
#ln -s /usr/bin/nodejs /usr/bin/node && \  
npm install -g @angular/cli && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

