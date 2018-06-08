FROM ubuntu:bionic  
  
MAINTAINER Rafael Ferreira da Silva <rafsilva@isi.edu>  
  
# add repositories  
RUN apt-get update  
  
# add wrench user  
RUN useradd --gid 100 --uid 550 --create-home --password wrench wrench  
  
# install compiler  
RUN apt-get -y install g++ gcc  
  
# set timezone  
RUN echo "America/Los_Angeles" > /etc/timezone && export
DEBIAN_FRONTEND=noninteractive && apt-get install -y tzdata  
  
# build environment  
RUN apt-get -y install pkg-config git cmake cmake-data doxygen doxygen-doc
doxygen-latex doxygen-gui graphviz libboost-all-dev wget  
RUN apt-get -y install sudo  
  
# configure coveralls  
RUN apt-get -y install lcov  
RUN gem install coveralls-lcov  
  
#################################################  
# WRENCH's dependencies  
#################################################  
# set root's environment variable  
ENV CXX="g++-7" CC="gcc-7"  
WORKDIR /tmp  
  
# install SimGrid  
RUN wget
https://gforge.inria.fr/frs/download.php/file/37452/SimGrid-3.19.tar.gz && tar
-xf SimGrid-3.19.tar.gz && cd SimGrid-3.19 && cmake . && make && sudo make
install && cd .. && rm -rf SimGrid-3.19*  
  
# install Lemon  
RUN wget http://lemon.cs.elte.hu/pub/sources/lemon-1.3.1.tar.gz && tar -xf
lemon-1.3.1.tar.gz && cd lemon-1.3.1 && cmake . && make && sudo make install
&& cd .. && rm -rf lemon-1.3.1*  
  
# install pugixml  
RUN wget
https://github.com/zeux/pugixml/releases/download/v1.8.1/pugixml-1.8.1.tar.gz
&& tar -xf pugixml-1.8.1.tar.gz && cd pugixml-1.8 && cmake . && make && sudo
make install && cd .. && rm -rf pugixml-1.8*  
  
# install json for modern c++  
RUN wget https://github.com/nlohmann/json/archive/v3.1.0.tar.gz && tar -xf
v3.1.0.tar.gz && cd json-3.1.0 && cmake . && make && sudo make install && cd
.. && rm -rf v3.1.0* json-3.1.0  
  
# install googletest  
RUN wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz &&
tar xf release-1.8.0.tar.gz && cd googletest-release-1.8.0/googletest && cmake
. && make && sudo make install && cd ../.. && rm -rf release-1.8.0.tar.gz
googletest-release-1.8.0  
  
#################################################  
# WRENCH's user  
#################################################  
USER wrench  
WORKDIR /home/wrench  
  
# set user's environment variable  
ENV CXX="g++-7" CC="gcc-7"  

