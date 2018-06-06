FROM alpine  
  
RUN apk add --no-cache \  
gcc \  
g++ \  
gfortran \  
musl-dev \  
git \  
gcovr \  
python2 \  
bash \  
autoconf \  
automake \  
libtool \  
make \  
curl  
  
RUN curl -SL https://www.open-
mpi.org/software/hwloc/v1.11/downloads/hwloc-1.11.9.tar.gz \  
| tar -xzC /tmp && \  
cd /tmp/hwloc-1.11.9 && \  
./configure && \  
make && \  
make install && \  
cd / && \  
rm -rf /tmp/hwloc-1.11.9  

