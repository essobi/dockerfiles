FROM tim03/gcc  
LABEL maintainer Chen, Wenli <chenwenli@chenwenli.com>  
WORKDIR /usr/src  
RUN \  
curl http://www.nasm.us/pub/nasm/releasebuilds/2.13.01/nasm-2.13.01.tar.xz |
tar Jxvf -  
RUN \  
cd nasm-2.13.01 && \  
./configure --prefix=/usr && make && make install && make clean  
  

