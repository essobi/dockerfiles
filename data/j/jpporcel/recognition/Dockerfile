FROM ubuntu:latest  
MAINTAINER Juan Pablo Porcel Porcel <juanpiporcel@gmail.com>  
EXPOSE 8080  
# Set working directory  
RUN mkdir /app  
WORKDIR /app  
  
# Update cache  
RUN apt-get update  
  
# Install git  
RUN apt-get install -y git  
  
# Install tools for C++  
RUN apt-get install -y build-essential  
RUN apt-get install -y cmake  
  
# Install framework pistache  
RUN apt-get install -y openssl  
RUN git clone https://github.com/oktal/pistache.git  
RUN cd pistache && mkdir build && cd build && cmake
-DCMAKE_CXX_FLAGS=-std=c++11 .. && make && make install && cd .. && cd ..  
  
ADD . /app  
  
RUN mkdir build && cd build && cmake -DCMAKE_CXX_FLAGS=-std=c++11 .. && make  
  
CMD build/server  

