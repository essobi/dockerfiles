FROM ubuntu:14.04  
MAINTAINER tym  
  
WORKDIR /workspace  
VOLUME /workspace  
RUN apt-get update && \  
apt-get install -y make g++ python git curl && \  
curl -sL https://deb.nodesource.com/setup | sudo bash - && \  
apt-get install -y nodejs && \  
npm -g install node-gyp codebox && \  
cd /usr/lib/node_modules/codebox/node_modules/shux/node_modules/pty.js && \  
make clean && \  
make  
  
ENV CODEBOX_USERNAME your_username  
ENV CODEBOX_PASSWORD password  
  
EXPOSE 8000  
ENTRYPOINT ["sh", "-c", "/usr/bin/codebox run -u
$CODEBOX_USERNAME:$CODEBOX_PASSWORD"]

