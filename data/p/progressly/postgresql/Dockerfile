FROM postgres:9.5.7  
  
RUN apt-get update \  
&& apt-get install -f -y \--no-install-recommends \  
software-properties-common \  
build-essential \  
pkg-config \  
git \  
postgresql-server-dev-9.5 \  
libproj-dev \  
&& apt-get clean && apt-get update && apt-get install -f -y \--no-install-
recommends \  
liblwgeom-dev \  
&& add-apt-repository "deb http://ftp.debian.org/debian testing main contrib"
\  
&& apt-get update && apt-get install -f -y \--no-install-recommends \  
libprotobuf-c-dev=1.2.* \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/eulerto/wal2json -b master --single-branch \  
&& cd /wal2json \  
&& make && make install \  
&& cd / \  
&& rm -rf wal2json  
  
COPY init/update_shared_preload_libraries.sh /docker-entrypoint-
initdb.d/update_shared_preload_libraries.sh  

