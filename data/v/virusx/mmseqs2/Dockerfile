FROM ubuntu:16.04  
ENV MMSEQS2_VERSION=4e96669bc  
RUN apt-get update && \  
apt-get install -y git build-essential make cmake vim-common libgomp1 gawk &&
\  
cd /root/ && \  
git clone https://github.com/soedinglab/MMseqs2 mmseqs2 && \  
cd mmseqs2 && \  
git checkout ${MMSEQS2_VERSION} && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=. .. && \  
make -j$(nproc) && \  
make install && \  
mv bin/mmseqs /usr/bin/ && \  
cd /root && \  
rm -rf /root/mmseqs2 && \  
apt-get purge -y git build-essential make cmake vim-common && \  
apt-get autoremove -y \--purge && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

