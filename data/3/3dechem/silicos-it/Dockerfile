FROM ubuntu:12.04  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
  
ENV BABEL_LIBDIR=/usr/lib/openbabel/2.3.0  
ENV BABEL_DATADIR=/usr/share/openbabel/2.3.0  
  
RUN apt-get update && apt-get install -y libopenbabel-dev libopenbabel4 build-
essential cmake wget && \  
mkdir /app && cd /app && \  
wget http://silicos-it.be.s3-website-eu-
west-1.amazonaws.com/_downloads/filter-it-1.0.2.tar.gz && \  
tar -zxf filter-it-1.0.2.tar.gz && \  
cd filter-it-1.0.2 && \  
mkdir build && cd build && \  
cmake .. && \  
make -j 2 && make install && \  
cd ../.. && \  
rm -r filter-it-1.0.2 filter-it-1.0.2.tar.gz && \  
wget http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/_downloads/strip-
it-1.0.2.tar.gz && \  
tar -zxf strip-it-1.0.2.tar.gz && \  
cd strip-it-1.0.2 && \  
mkdir build && cd build && \  
cmake .. && \  
make -j 2 && make install && \  
cd ../.. && \  
rm -r strip-it-1.0.2 strip-it-1.0.2.tar.gz && \  
wget http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/_downloads/shape-
it-1.0.1.tar.gz && \  
tar -zxf shape-it-1.0.1.tar.gz && \  
cd shape-it-1.0.1/ && \  
mkdir build && cd build && \  
cmake .. && \  
make -j 2 && make install && \  
cd ../.. && \  
rm -r shape-it-1.0.1 shape-it-1.0.1.tar.gz && \  
wget http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/_downloads/align-
it-1.0.4.tar.gz && \  
tar -zxf align-it-1.0.4.tar.gz && \  
cd align-it-1.0.4/ && \  
perl -pi -e 's@/openbabel-2.0@@' cmake/modules/FindOpenBabel2.cmake && \  
mkdir build && cd build && \  
BABEL_INCLUDEDIR=/usr/include/openbabel-2.0 cmake .. && \  
make -j 2 && make install && \  
cd ../.. && \  
rm -r align-it-1.0.4 align-it-1.0.4.tar.gz && \  
apt-get remove -y libopenbabel-dev build-essential cmake && apt-get autoremove
-y  

