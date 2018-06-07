FROM ubuntu:14.04  
RUN sudo apt-get -y update  
RUN apt-get install -y g++ autoconf qt4-dev-tools patch libtool make git  
RUN apt-get install -y software-properties-common python-software-properties  
  
# fix to get cmake 3.x in ubuntu 14.04  
RUN add-apt-repository ppa:george-edison55/cmake-3.x  
RUN sudo apt-get remove -y cmake cmake-data  
RUN sudo -E apt-get update  
RUN apt-get install -y cmake  
  
# install dependencies  
RUN apt-get install -qq libsvm-dev libglpk-dev libzip-dev zlib1g-dev
libxerces-c-dev libbz2-dev  
RUN apt-get install -qq libboost-date-time1.54-dev \  
libboost-iostreams1.54-dev \  
libboost-regex1.54-dev \  
libboost-math1.54-dev \  
libboost-random1.54-dev  
  
RUN git clone https://github.com/OpenMS/contrib.git  
RUN mkdir contrib-build  
  
WORKDIR /contrib-build  
  
RUN cmake -DBUILD_TYPE=SEQAN ../contrib  
RUN cmake -DBUILD_TYPE=WILDMAGIC ../contrib  
RUN cmake -DBUILD_TYPE=EIGEN ../contrib  
RUN cmake -DBUILD_TYPE=COINOR ../contrib  
RUN cmake -DBUILD_TYPE=SQLITE ../contrib  
  

