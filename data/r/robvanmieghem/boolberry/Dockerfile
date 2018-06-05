FROM ubuntu:16.04  
LABEL maintainer "Rob Van Mieghem <robvanmieghem@gmail.com>"  
  
RUN apt-get update  
RUN apt-get install -y apt-utils  
RUN apt-get -y install gcc-4.8 g++-4.8 libboost1.58-all-dev git cmake  
RUN apt-get -y install build-essential  
RUN git clone https://github.com/cryptozoidberg/boolberry.git  
RUN cd boolberry; make  
  
RUN mkdir /boolb  
  
EXPOSE 10101  
ENTRYPOINT ["/boolberry/build/release/src/boolbd","--data-dir","/boolb"]  

