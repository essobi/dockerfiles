FROM ubuntu:xenial  
  
# install dependencies  
RUN apt-get update  
RUN apt-get install -y autotools-dev automake build-essential texinfo nodejs
npm git wget vim  
  
# link the nodejs to node to avoid nasty bug, since frida hardcodes the path  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# download frida  
RUN mkdir -p /srv  
WORKDIR /srv  
RUN git clone https://github.com/frida/frida  
WORKDIR /srv/frida  
RUN git submodule init  
RUN git submodule update  
  
# cause the core to be dumped if segmentation fault occurs  
RUN ulimit -c unlimited  
  
# build sdk  
RUN make -f Makefile.sdk.mk  
  
# run tests  
#RUN make check-gum-64  

