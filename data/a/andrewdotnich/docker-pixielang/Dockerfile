FROM ubuntu:latest  
  
RUN apt-get update  
  
RUN apt-get install -yy libffi-dev libedit-dev libuv-dev libboost-all-dev git
build-essential  
  
WORKDIR /usr/local/src  
  
RUN git clone https://github.com/pixie-lang/pixie.git  
  
WORKDIR /usr/local/src/pixie  
  
RUN apt-get install -yy curl python-pip pkg-config  
  
RUN make build_with_jit  
  
RUN ln -s /usr/local/src/pixie/pixie-vm /usr/local/bin/pixie-vm  
  
WORKDIR /usr/local/src  
  
RUN git clone https://github.com/pixie-lang/dust  
  
RUN ln -s /usr/local/src/dust/dust /usr/local/bin/dust  

