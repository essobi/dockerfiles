FROM spitzenidee/postgresql_base:10.3  
MAINTAINER Michael Spitzer <professa@gmx.net>  
  
#######################################################################  
# Prepare the environment for the TimescaleDB compilation:  
ENV TIMESCALEDB_VERSION "0.9.1"  
  
#######################################################################  
# Prepare the build requirements for the rdkit compilation:  
RUN apt-get update && apt-get install -y --no-install-recommends \  
postgresql-server-dev-all \  
wget \  
cmake \  
build-essential && \  
# Install TimescaleDB:  
mkdir /build && \  
cd /build && \  
wget
https://github.com/timescale/timescaledb/archive/$TIMESCALEDB_VERSION.tar.gz
&& \  
tar xzvf $TIMESCALEDB_VERSION.tar.gz && \  
cd timescaledb-$TIMESCALEDB_VERSION && \  
./bootstrap && \  
cd build/ && \  
make && \  
make install && \  
# Clean up again:  
cd / && \  
rm -rf /build && \  
apt-get remove -y wget cmake build-essential && \  
apt-get autoremove --purge -y && \  
apt-get clean && \  
apt-get purge && \  
rm -rf /var/lib/apt/lists/*  
# Done.  

