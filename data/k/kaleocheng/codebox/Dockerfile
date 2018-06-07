FROM debian  
MAINTAINER kaleocheng  
  
WORKDIR /workspace  
VOLUME /workspace  
RUN apt-get update && \  
apt-get install -y make g++ python python-virtualenv git curl && \  
curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get install -y nodejs && \  
npm -g install node-gyp codebox && \  
cd /usr/lib/node_modules/codebox/node_modules/shux/node_modules/pty.js && \  
make clean && \  
make  
  
ENV ACCOUNT user1:passwd1,user2:passwd2  
  
EXPOSE 8000  
ENTRYPOINT ["sh", "-c", "/usr/bin/codebox run -u $ACCOUNT"]  

