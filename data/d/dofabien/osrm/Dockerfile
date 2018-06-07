FROM ubuntu:14.04  
RUN apt-get update  
  
RUN apt-get install -y build-essential git cmake pkg-config libprotoc-dev
libprotobuf8 \  
protobuf-compiler libprotobuf-dev libosmpbf-dev libpng12-dev \  
libbz2-dev libstxxl-dev libstxxl-doc libstxxl1 libxml2-dev \  
libzip-dev libboost-all-dev lua5.1 liblua5.1-0-dev libluabind-dev
libluajit-5.1-dev libtbb-dev  
  
RUN \  
git clone https://github.com/Project-OSRM/osrm-backend.git /src && \  
mkdir -p /build && \  
cd /build && \  
cmake /src && make && \  
mv /src/profiles/bicycle.lua profile.lua && \  
mv /src/profiles/lib/ lib && \  
echo 'disk=/data/stxxl,0,syscall' > /build/.stxxl  
  
ADD run.sh /usr/bin/run.sh  
RUN mkdir -p /data  
  
RUN cd /data  
  
VOLUME /data  
  
RUN chmod -R 777 /data  
  
ENV PROFILE_LUA car.lua  
ENV FILE_OSM null  
ENV REFRESH 0  
WORKDIR /build  
ADD run.sh /build/run.sh  
RUN chmod 755 /build/run.sh  
EXPOSE 5000  
CMD ./run.sh  

