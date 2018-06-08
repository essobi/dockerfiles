FROM coduno/base  
  
RUN mkdir /node  
RUN apt-get update -y && apt-get install -y wget && wget -O /node/node.tar.gz
https://nodejs.org/dist/v5.7.1/node-v5.7.1-linux-x64.tar.gz  
RUN tar -xzf /node/node.tar.gz  
  
ADD . /run  

