FROM ubuntu:12.04  
COPY . /src  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN cd /src && apt-get update && apt-get install -y git-core build-essential
&& git submodule update --init && apt-get install -y curl && curl -sL
https://deb.nodesource.com/setup | bash - && apt-get install -y nodejs && npm
install  
  
EXPOSE 8888  
CMD cd /src && node static.js  

