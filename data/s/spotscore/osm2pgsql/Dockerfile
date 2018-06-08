FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
libtool \  
make \  
g++ \  
pkg-config \  
libboost-dev \  
libboost-system-dev \  
libboost-filesystem-dev \  
libboost-thread-dev \  
libexpat1-dev \  
libgeos-dev \  
libgeos++-dev \  
libpq-dev \  
libbz2-dev \  
libproj-dev \  
zlib1g-dev \  
lua5.2 \  
liblua5.2-dev\  
git  
  
  
RUN git clone https://github.com/openstreetmap/osm2pgsql.git /osm2pgsql  
  
WORKDIR /osm2pgsql  
  
RUN ./autogen.sh && ./configure && make && make install  
  
CMD osm2pgsql --help  

