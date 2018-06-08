FROM node:argon  
MAINTAINER WOW! Group Development  
  
WORKDIR /app  
ADD index.js package.json /app/  
ADD runner /  
RUN npm install \  
&& curl -sSL -o /usr/local/bin/gosu
https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64 \  
&& curl -sSL -o /usr/local/bin/tini
https://github.com/krallin/tini/releases/download/v0.9.0/tini \  
&& chmod +x /usr/local/bin/gosu \  
&& chmod +x /usr/local/bin/tini  
  
ENTRYPOINT ["/runner"]  

