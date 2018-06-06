FROM ubuntu  
  
RUN apt-get update && apt-get install -y \  
autoconf \  
build-essential \  
cmake \  
genisoimage \  
git \  
libssl-dev \  
zlib1g-dev  
  
# Clone and build libmdg-hfsplus  
RUN git clone \--depth=1 https://github.com/planetbeing/libdmg-hfsplus.git  
RUN cd libdmg-hfsplus && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/bin . && \  
make && \  
make install && \  
cd \- && rm -r libdmg-hfsplus  
  
COPY create-dmg.sh .  
  
ENTRYPOINT ["/bin/bash", "/create-dmg.sh"]  

