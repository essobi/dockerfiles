FROM debian:stretch  
RUN apt-get update -qq && apt-get install -y \  
postgresql-9.6 postgresql-server-dev-9.6 \  
build-essential autoconf libtool \  
libproj-dev libgdal-dev libgeos-dev \  
libprotobuf-c-dev protobuf-c-compiler \  
curl  
  
RUN service postgresql start && su -l postgres -c "createuser -s `whoami`"  
  
RUN curl --silent -L \  
https://github.com/postgis/postgis/archive/d977a1e486494769eb7e69a7359482c406d2785a.tar.gz
| \  
tar xz && cd postgis-d977a1e486494769eb7e69a7359482c406d2785a && \  
./autogen.sh && \  
./configure --without-address-standardizer --without-raster --without-topology
&& make && make install && \  
cd .. && rm postgis-d977a1e486494769eb7e69a7359482c406d2785a -rf  

