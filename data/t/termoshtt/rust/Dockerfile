FROM rust:1.22  
MAINTAINER termoshtt <toshiki.teramura@gmail.com>  
RUN apt-get update -qq && apt-get -y -qq install \  
curl gcc gfortran make cmake binutils-dev \  
sqlite3 libsqlite3-dev \  
libcurl4-openssl-dev libelf-dev libdw-dev libiberty-dev \  
&& apt-get clean  
RUN wget https://github.com/SimonKagstrom/kcov/archive/master.tar.gz && \  
tar xzf master.tar.gz && \  
mkdir -p kcov-master/build && \  
cd kcov-master/build && \  
cmake .. && make && make install && \  
rm -rf ../../kcov-master  

