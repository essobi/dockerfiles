FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
g++ \  
libboost-dev \  
make  
  
COPY . /pubtcrs  
WORKDIR /pubtcrs  
CMD make && cd test && sh runall.bash  

