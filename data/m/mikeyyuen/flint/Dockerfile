FROM ubuntu:14.04  
  
MAINTAINER Michael Yuen <michael.yuen@mac.com>  
  
COPY ./flint-plus-plus flint-plus-plus  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y \  
g++ \  
make  
  
RUN cd flint-plus-plus/flint && \  
make  
  
ENTRYPOINT [ "/flint-plus-plus/flint/flint++", "-r", "/src" ]  
  

