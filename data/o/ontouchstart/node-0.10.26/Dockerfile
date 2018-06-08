FROM debian:sid  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install python g++ make checkinstall git vim  
RUN git clone https://github.com/joyent/node.git  
RUN cd node && git checkout v0.10.26-release && ./configure && make install  
  

