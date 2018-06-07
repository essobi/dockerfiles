FROM spitzenidee/postgresql_rdkit:latest  
MAINTAINER Michael Spitzer <professa@gmx.net>  
  
#######################################################################  
# DockerHub / GitHub:  
# https://hub.docker.com/r/spitzenidee/postgresql_rdkit_timescaledb/  
# https://github.com/spitzenidee/postgresql_rdkit_timescaledb  
#######################################################################  
  
#######################################################################  
# Prepare the environment for the TimescaleDB compilation:  
ENV TIMESCALEDB_VERSION 0.5.0  
  
#######################################################################  
# Prepare the build requirements for the rdkit compilation:  
RUN apt-get update && apt-get install -y \  
postgresql-server-dev-all \  
git \  
cmake \  
build-essential && \  
# Install TimescaleDB:  
mkdir /build && \  
cd /build && \  
git clone --single-branch -b $TIMESCALEDB_VERSION
https://github.com/timescale/timescaledb.git && \  
cd /build/timescaledb && \  
make && \  
make install && \  
cd / && \  
rm -rf /build && \  
# Clean up again:  
apt-get remove -y git cmake build-essential && \  
apt-get autoremove --purge -y && \  
apt-get clean && \  
apt-get purge && \  
rm -rf /var/lib/apt/lists/*  
  
# Done.  

