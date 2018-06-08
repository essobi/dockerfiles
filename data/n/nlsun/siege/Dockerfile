FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y \  
wget \  
cmake \  
gcc \  
&& \  
mkdir siege && \  
cd siege && \  
wget http://download.joedog.org/siege/siege-4.0.2.tar.gz && \  
tar -xvf siege-4.0.2.tar.gz && \  
cd siege-* && \  
./configure && \  
make && \  
make install && \  
cd / && \  
apt-get remove -y \  
cmake \  
gcc \  
&& \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  

