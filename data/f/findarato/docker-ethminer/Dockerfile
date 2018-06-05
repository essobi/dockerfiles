FROM nvidia/cuda:8.0-devel-ubuntu16.04  
LABEL "version":"1.0" \  
"maintainer":"Joseph harry"  
  
WORKDIR /  
  
# Package and dependency setup  
RUN apt-get update \  
&& apt-get -y install software-properties-common \  
&& add-apt-repository -y ppa:ethereum/ethereum -y \  
&& apt-get update \  
&& apt-get install -y git \  
cmake \  
libcryptopp-dev \  
libleveldb-dev \  
libjsoncpp-dev \  
libjsonrpccpp-dev \  
libboost-all-dev \  
libgmp-dev \  
libreadline-dev \  
libcurl4-gnutls-dev \  
ocl-icd-libopencl1 \  
opencl-headers \  
mesa-common-dev \  
libmicrohttpd-dev \  
build-essential  
  
# Git repo set up  
RUN git clone https://github.com/ethereum-mining/ethminer.git; \  
cd ethminer; \  
git checkout tags/v0.11.0  
  
# Build  
RUN cd ethminer; \  
mkdir build; \  
cd build; \  
cmake .. -DETHASHCUDA=ON -DETHSTRATUM=ON -DAPICORE=ON; \  
cmake --build . -j4; \  
make install;  
  
# Env setup  
ENV GPU_FORCE_64BIT_PTR=0 \  
GPU_MAX_HEAP_SIZE=100 \  
GPU_USE_SYNC_OBJECTS=1 \  
GPU_MAX_ALLOC_PERCENT=100 \  
GPU_SINGLE_ALLOC_PERCENT=100  
ENTRYPOINT ["/usr/local/bin/ethminer", "--farm-recheck","2000","-U" ]  
  
EXPOSE 80  

