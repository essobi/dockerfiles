FROM ubuntu:xenial  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y curl git bzip2 && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
npm install -g foundation-cli && \  
npm install -g bower && \  
rm -r /root/.npm  

