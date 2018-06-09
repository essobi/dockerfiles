FROM ubuntu  
MAINTAINER Rafael de Morais "rdemorais.freitas@gmail.com"  
RUN apt-get update && \  
apt-get install -y curl --no-install-recommends && \  
curl -k -L https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs --no-install-recommends && \  
apt-get install -y build-essential && \  
npm install pm2 -g && \  
mkdir /opt/workapp && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

