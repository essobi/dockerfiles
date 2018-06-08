#Container with debug possibilites, no optimalisation or other extras and as
little as possible reliance on external libs for calculations  
#As little as possible extra software: only the necassary for building,
debugging, a terminal, a editor and ssh for graphical debugging with
X-forwarding  
FROM ubuntu:18.04  
RUN apt-get update && apt-get -y install autoconf curl ddd gfortran git
libtool make python-dev ssh vim && apt-get --purge autoremove && rm -r
/var/cache/apt/archives  
RUN cd /root && git clone https://github.com/ngaro/abinit.git  
WORKDIR /root/abinit  
RUN ./autogen.sh  
RUN ./configure --enable-debug=naughty --enable-mpi=no  
RUN make  
RUN make check  
RUN make install  

