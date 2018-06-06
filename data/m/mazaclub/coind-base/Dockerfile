FROM phusion/baseimage  
# IMAGE mazaclub/coind-base  
ENV BUILDER DOCKERHUB  
COPY atomic.patch /  
RUN apt-get update \  
&& apt-get install -y libboost-all-dev \  
dh-autoreconf \  
libcurl4-openssl-dev \  
git apg libboost-all-dev build-essential  
  
RUN curl http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz -o
db-4.8.30.NC.tar.gz \  
&& tar -xf db-4.8.30.NC.tar.gz \  
&& cd db-4.8.30.NC/dbinc \  
&& mv /atomic.patch . \  
&& patch < atomic.patch \  
&& cd ..//build_unix \  
&& mkdir -p build \  
&& BDB_PREFIX=$(pwd)/build \  
&& ../dist/configure --disable-shared --enable-cxx --with-pic
--prefix=$BDB_PREFIX \  
&& make install  
# BDB4.8 does not appear to correctly support multiple makejobs  
RUN cd / \  
&& rm -rf /etc/service/* \  
&& apt-get autoremove -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV BDB_PREFIX=/db-4.8.30.NC/build_unix/build  
COPY . /  

