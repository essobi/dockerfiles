FROM debian:wheezy  
  
RUN apt-get update && \  
apt-get install -y cmake libboost-dev libboost-filesystem-dev libboost-
iostreams-dev libboost-program-options-dev \  
libboost-regex-dev libboost-system-dev libboost-thread-dev libluabind-dev
libxml2-dev libstxxl-dev \  
libosmpbf-dev libprotobuf-dev libbz2-dev libtbb-dev make && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY . /src  
  
RUN mkdir -p /build && \  
cd /build && \  
cmake -DOSRM_HAS_ELEVATION:BOOL=ON ../src && \  
make -j8 install && \  
cd / && \  
rm -r /build && \  
strip /usr/local/bin/*  
  
EXPOSE 80  
ENV OSRM_CONFIG /data/data.osrm  
ENV OSRM_VERSION=0.4.1  
VOLUME /data  
  
CMD /src/docker-start.sh  

