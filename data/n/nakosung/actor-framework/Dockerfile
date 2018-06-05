FROM ubuntu:14.04  
MAINTAINER deif79@gmail.com  
  
RUN apt-get update -y  
RUN apt-get install build-essential git -y  
  
# Get modern cmake  
RUN apt-get install wget -yq  
RUN wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz; \  
tar xzvf cmake-3.2.2.tar.gz; \  
cd cmake-3.2.2; \  
./configure --prefix=/usr/local/cmake; \  
make && make install; \  
cd ..; \  
rm -rf cmake-3.2.2  
  
ENV PATH /usr/local/cmake/bin:${PATH}  
  
RUN apt-get install libprotobuf-dev libpthread-stubs0-dev -y  
RUN git clone https://github.com/actor-framework/actor-framework.git  
RUN cd actor-framework; ./configure && make && make install  
ENV LD_LIBRARY_PATH /usr/local/lib:${LD_LIBRARY_PATH}

