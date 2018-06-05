FROM debian:wheezy  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update  
RUN apt-get install -y curl build-essential git zip m4 openssl libssl-dev git
libjson0 libjson0-dev libcurl4-openssl-dev wget  
RUN apt-get clean  
WORKDIR /usr/src  
RUN wget http://mirrors.kernel.org/gnu/gmp/gmp-5.1.3.tar.bz2 && tar xjvf
gmp-5.1.3.tar.bz2 && cd gmp-5.1.3 && ./configure --enable-cxx && make -j4 &&
make install && ldconfig  
RUN git clone https://github.com/arbedout/fastrie.git && cd fastrie/xptMiner
&& make clean LD_LIBRARY_PATH=/usr/local/lib && make -j4 -f Makefile_mtune  
CMD /usr/src/fastrie/xptMiner/xptminer -u username.riecoinworkername -p
workerpassword  

