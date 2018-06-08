FROM node:6.11.3-slim  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y yarn=1.1.0-1 && \  
apt-get remove \--purge -y apt-transport-https && \  
rm /etc/apt/sources.list.d/yarn.list && \  
rm -rf /var/lib/apt/lists/*  

