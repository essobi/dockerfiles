# Start from debain base image  
FROM debian:latest  
  
# Install vim  
RUN apt-get update && apt-get upgrade && apt-get install -y vim  
  
# Install build-essential  
RUN apt-get install -y build-essential  
  
#Install git  
RUN apt-get install -y git-core  
  
#install boost dev package  
RUN apt-get install -y libboost-all-dev  
  
#Install cmake  
RUN apt-get install -y cmake  
  
#Clone brewer repo  
RUN git clone https://github.com/erostamas/brewer.git  
  
#Navigate to build directory  
WORKDIR /brewer/build  
RUN cmake ../  
RUN ../tools/build_brewer.sh  
  

