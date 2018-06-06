FROM debian:jessie  
RUN apt-get -y update && \  
apt-get -y install llvm cmake git clang zlib1g-dev libedit-dev pkg-config && \  
apt-get -y clean && \  
git clone https://github.com/tomhrr/dale.git && \  
mkdir build && \  
cd build && \  
cmake ../dale && \  
make && \  
make install  

