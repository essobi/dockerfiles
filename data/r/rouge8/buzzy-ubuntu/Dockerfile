FROM ubuntu:12.04  
MAINTAINER Andy Freeland <andy.freeland@redjack.com>  
  
RUN apt-get update  
RUN apt-get install -y cmake build-essential git sudo  
RUN git clone \--recursive https://github.com/redjack/buzzy.git  
RUN mkdir buzzy/.build  
RUN cd buzzy/.build && cmake ..  
RUN cd buzzy/.build && make  
RUN cd buzzy/.build && ./src/buzzy install  

