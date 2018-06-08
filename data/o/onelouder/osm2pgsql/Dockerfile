# DOCKER-VERSION 1.5.0  
# VERSION 0.2  
FROM debian:wheezy  
MAINTAINER Mark Snyder <marksnyder@level11.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
g++ \  
git-core \  
libboost-dev \  
libboost-filesystem-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libbz2-dev \  
libgeos++-dev \  
libgeos-dev \  
liblua5.2-dev \  
libpq-dev \  
libproj-dev \  
libprotobuf-c0-dev \  
libtool \  
libxml2-dev \  
lua5.2 \  
make \  
protobuf-c-compiler \  
curl &&\  
rm -rf /var/lib/apt/lists/*  
  
ENV HOME /root  
ENV OSM2PGSQL_VERSION 0.87.2  
ENV PG_HOST $PG_HOST  
ENV PG_PORT $PG_PORT_5432_TCP_PORT  
ENV PG_ENV_OSM_DB $PG_ENV_OSM_DB  
ENV PG_ENV_OSM_USER $PG_ENV_OSM_USER  
ENV PGPASS $PGPASS  
  
RUN mkdir src &&\  
cd src &&\  
git clone \--depth 1 --branch $OSM2PGSQL_VERSION
https://github.com/openstreetmap/osm2pgsql.git &&\  
cd osm2pgsql &&\  
./autogen.sh &&\  
./configure &&\  
make &&\  
make install &&\  
cd /root &&\  
rm -rf src  
  
RUN mkdir /maps  
RUN echo \  
"*:$PG_ENV_PORT_5432_TCP_PORT:$PG_ENV_OSM_DB:$PG_ENV_OSM_USER:$PGPASS" >
/root/.pgpass &&\  
chmod 0600 /root/.pgpass  
  
RUN echo \  
"*:$PG_ENV_PORT_5432_TCP_PORT:$PG_ENV_OSM_DB:$PG_ENV_OSM_USER:$PGPASS" >
/home/.pgpass &&\  
chmod 0600 /home/.pgpass  
  
ADD processFiles.sh /root/processFiles.sh  
ENTRYPOINT /root/processFiles.sh  

