FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y linux-tools-generic unzip libbz2-dev python-dev scons\  
libtool liblzma-dev libblas-dev make automake \  
ccache libcppunit-dev doxygen \  
libcrypto++-dev libACE-dev gfortran liblapack-dev \  
libevent-dev libssh2-1-dev libicu-dev libv8-dev \  
g++ google-perftools libgoogle-perftools-dev \  
zlib1g-dev git pkg-config valgrind autoconf \  
libcurl4-openssl-dev cmake libsigc++-2.0-dev  
RUN mkdir -p $HOME/local/bin  
RUN export PATH="$HOME/local/bin:$PATH"  
  
RUN mkdir -p $HOME/local/lib  
RUN export LD_LIBRARY_PATH="$HOME/local/lib:$LD_LIBRARY_PATH"  
  
RUN export PKG_CONFIG_PATH="$HOME/local/lib/pkgconfig/:$HOME/local/lib/pkg-
config/"  
  
# get rtbkit-deps  
RUN git clone https://github.com/connectedinteractive/rtbkit-deps.git  
RUN cd rtbkit-deps && git submodule update --init && make all NODEJS_ENABLED=0  
  
# get rtbkit  
RUN git clone https://github.com/connectedinteractive/rtbkit.git  
RUN cd rtbkit && cp jml-build/sample.local.mk local.mk && make compile
NODEJS_ENABLED=0 && make test NODEJS_ENABLED=0  

