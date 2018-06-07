FROM ubuntu:latest  
  
RUN apt-get update && \  
apt-get install -y wget nodejs npm openssl zip vim-common git && \  
#nodejs, npm gulp install  
npm cache clean && \  
npm install n -g && \  
n stable && \  
ln -sf /usr/local/bin/node /usr/bin/node && \  
npm update -g npm && \  
npm install -g gulp  
  
COPY crx_build.sh /usr/bin/  
  
VOLUME /app  
WORKDIR /app  
CMD ["bash"]  

