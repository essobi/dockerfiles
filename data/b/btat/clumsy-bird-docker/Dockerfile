FROM ubuntu:12.04  
COPY . /src  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN cd /src && apt-get update && apt-get install -y curl && curl -sL
https://deb.nodesource.com/setup | bash - && apt-get install -y nodejs && npm
install -g grunt-cli && npm install  
  
EXPOSE 8001  
CMD cd /src && grunt connect  

