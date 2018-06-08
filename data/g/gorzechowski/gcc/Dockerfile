FROM ubuntu:xenial  
  
RUN apt-get update && apt-get -y install software-properties-common  
  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
  
RUN apt-get update && apt-get -y --allow-unauthenticated install \  
g++ \  
gcc \  
make \  
cmake  

