FROM ubuntu:16.04  
MAINTAINER Stepan Kuzmin <to.stepan.kuzmin@gmail.com>  
  
ENV OSRM_VERSION 5.7.0  
RUN apt-get -yqq update \  
&& apt-get -yqq install \  
build-essential \  
cmake \  
curl \  
libboost-all-dev \  
libbz2-dev \  
liblua5.2-dev \  
libluabind-dev \  
libstxxl-dev \  
libstxxl1v5 \  
libtbb-dev \  
libxml2-dev \  
libzip-dev \  
lua-sql-postgres \  
lua-sql-postgres-dev \  
lua5.2 \  
pkg-config  
  
RUN mkdir -p /usr/src/osrm-backend/build \  
&& curl -SLO "https://github.com/Project-OSRM/osrm-
backend/archive/v$OSRM_VERSION.tar.gz" \  
&& tar xzf "v$OSRM_VERSION.tar.gz" \--strip-components 1 -C /usr/src/osrm-
backend \  
&& rm "v$OSRM_VERSION.tar.gz" \  
&& cd /usr/src/osrm-backend/build \  
&& cmake .. -DCMAKE_BUILD_TYPE=Release \  
&& cmake --build . \  
&& cmake --build . --target install \  
&& mkdir /data \  
&& mkdir /profiles \  
&& mkdir /extracts \  
&& cp -r /usr/src/osrm-backend/profiles/* /profiles \  
&& rm -rf /usr/src/osrm-backend  
  
COPY entrypoint.sh entrypoint.sh  
COPY profiles/* /profiles  
  
EXPOSE 5000  
VOLUME /data  
VOLUME /profiles  
VOLUME /extracts  
  
ENTRYPOINT ["/entrypoint.sh"]  

