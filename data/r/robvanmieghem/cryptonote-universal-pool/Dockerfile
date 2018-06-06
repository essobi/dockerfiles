FROM ubuntu:14.04  
LABEL maintainer "Rob Van Mieghem <robvanmieghem@gmail.com>"  
  
RUN apt-get update  
RUN apt-get -y install apt-utils  
RUN apt-get -y install git libboost1.54-all-dev nodejs-dev nodejs-legacy npm
cmake libssl-dev  
RUN apt-get -y install build-essential  
RUN cd /  
RUN git clone https://github.com/robvanmieghem/cryptonote-universal-pool.git  
RUN cd /cryptonote-universal-pool; npm update  
  
EXPOSE 80  
WORKDIR /cryptonote-universal-pool  
ENTRYPOINT ["node","init.js"]  

