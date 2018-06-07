FROM johntfoster/netcdf:largefiles  
  
MAINTAINER John Foster <johntfosterjr@gmail.com>  
  
ENV HOME /root  
  
RUN apt-get -yq install g++ \  
gfortran \  
python \  
libblas-dev \  
liblapack-dev \  
libboost-dev  
  
#Get modern cmake  
RUN wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz; \  
tar xzvf cmake-3.2.2.tar.gz; \  
cd cmake-3.2.2; \  
./configure --prefix=/usr/local/cmake; \  
make && make install; \  
cd ..; \  
rm -rf cmake-3.2.2  
  
#Build Trilinos  
RUN wget
http://trilinos.csbsju.edu/download/files/trilinos-11.14.2-Source.tar.bz2; \  
tar xjvf trilinos-11.14.2-Source.tar.bz2; \  
mkdir trilinos-11.14.2-Source/build  
ADD trilinos-debian-cmake.sh /trilinos-11.14.2-Source/build/trilinos-debian-
cmake.sh  
RUN cd trilinos-11.14.2-Source/build; \  
./trilinos-debian-cmake.sh; \  
make && make install; \  
cd ../..; \  
rm -rf trilinos-11.14.2-Source trilinos-11.14.2-Source.tar.bz2  
  

