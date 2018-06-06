FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y git  
RUN cd /tmp; git clone git://github.com/ecell/ecell3  
RUN apt-get install -y autoconf libtool  
RUN apt-get install -y g++ libgsl0-dev python-numpy python-ply python-gtk2-dev
libboost-random-dev libboost-python-dev  
RUN cd /tmp/ecell3; sh autogen.sh && ./configure && make && make install  

