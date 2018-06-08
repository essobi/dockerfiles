FROM ubuntu:13.10  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository -y ppa:ubuntu-toolchain-r/ppa  
RUN apt-add-repository -y 'deb http://llvm.org/apt/saucy/ llvm-toolchain-saucy
main'  
RUN apt-add-repository -y 'deb http://llvm.org/apt/saucy/ llvm-toolchain-
saucy-3.4 main'  
RUN apt-add-repository -y 'deb http://ppa.launchpad.net/ubuntu-
toolchain-r/test/ubuntu saucy main'  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 15CF4D18AF4F7421  
RUN apt-add-repository -y 'deb http://archive.ubuntu.com/ubuntu saucy
universe'  
RUN apt-add-repository -y ppa:chris-lea/node.js  
  
RUN apt-get update  
RUN apt-get install -y libcap-dev pkg-config clang-3.4 subversion build-
essential git autoconf libtool nodejs curl  
  
RUN mkdir /src  
  
ENV CXX clang++  
  
RUN cd /src && curl -L
https://github.com/jedisct1/libsodium/archive/0.4.5.tar.gz | tar xz  
RUN cd /src/libsodium-0.4.5 && ./autogen.sh && ./configure && make && make
check && make install  
  
RUN curl https://install.meteor.com/ | sh -x  
  
RUN cd /src && curl -L
https://github.com/kentonv/capnproto/archive/master.tar.gz | tar xz  
# Would "make -j6 check", but tests are broken when there's no global scope
ipv6 address assigned to an interface.  
# See <https://github.com/kentonv/capnproto/issues/72>.  
RUN cd /src/capnproto-master && cd c++ && ./setup-autotools.sh && autoreconf
-i && ./configure && make -j6 && make install  
  
RUN cd /src && curl -L
https://github.com/kentonv/sandstorm/archive/master.tar.gz | tar xz  
RUN cd /src/sandstorm-master && make && make install
SANDSTORM_USER=nobody:nogroup  

