FROM ubuntu:16.04  
  
MAINTAINER Michele Sevegnani <michele.sevegnani@glasgow.ac.uk>  
  
# Install debs  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy --no-install-recommends install \  
build-essential \  
ocaml-native-compilers \  
ocaml-findlib \  
cmake \  
libm4ri-dev \  
git-core \  
zlib1g-dev \  
vim-common \  
ca-certificates && \  
DEBIAN_FRONTEND=noninteractive apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /home/CMSat  
  
WORKDIR /home/CMSat  
  
# Install CryptoMiniSat  
RUN git clone https://github.com/msoos/cryptominisat.git && \  
cd cryptominisat && \  
git checkout 5.0.1 && \  
mkdir build && \  
cd build && \  
cmake -DUSE_GAUSS=ON .. && \  
make -j4 && \  
make install && \  
ldconfig  
  
CMD [ "sh" ]  

