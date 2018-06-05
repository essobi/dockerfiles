FROM node:8.3-alpine  
  
RUN apk add --no-cache git docker && \  
npm install -g bower grunt-cli less && \  
echo '{ "allow_root": true }' > /root/.bowerrc && \  
mkdir -p /.config && \  
chmod 777 /.config && \  
mkdir -p /.local && \  
chmod 777 /.local && \  
mkdir -p /.cache && \  
chmod 777 /.cache && \  
mkdir -p /.npm && \  
chmod 777 /.npm  
WORKDIR /data  

