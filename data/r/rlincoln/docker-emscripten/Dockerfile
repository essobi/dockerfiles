FROM ubuntu:latest  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
WORKDIR /  
  
RUN apt-get update && apt-get install -y build-essential curl git cmake python
&&\  
curl -sL https://deb.nodesource.com/setup | bash - && apt-get install -y
nodejs &&\  
apt-get clean  
RUN curl https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-
portable.tar.gz >\  
emsdk-portable.tar.gz && tar xzf emsdk-portable.tar.gz && pushd emsdk_portable
&&\  
./emsdk update && ./emsdk install latest && ./emsdk activate latest  

