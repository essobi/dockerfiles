FROM ubuntu:16.04  
ENV NONPAREIL_VERSION="v2.4.01"  
RUN apt-get update && \  
apt-get install -y git build-essential make r-base && \  
cd /root/ && \  
git clone https://github.com/lmrodriguezr/nonpareil nonpareil && \  
cd nonpareil && \  
git checkout ${NONPAREIL_VERSION} && \  
make -j$(nproc) && \  
make install && \  
cd /root && \  
rm -rf /root/nonpareil && \  
apt-get purge -y git build-essential make && \  
apt-get autoremove -y \--purge && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

