FROM ubuntu:16.04  
# Bitcoin gold build environment  
# Base  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
build-essential \  
libtool \  
autotools-dev \  
automake \  
pkg-config \  
bsdmainutils \  
python3  
  
WORKDIR /root/  
RUN git clone https://github.com/BTCGPU/BTCGPU  
WORKDIR /root/BTCGPU/depends  
RUN make -j 4  
WORKDIR /root/BTCGPU  
  
CMD ["/bin/bash"]  

