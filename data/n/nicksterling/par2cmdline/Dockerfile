FROM ubuntu:16.04  
  
WORKDIR /data  
  
RUN apt-get update && \  
apt-get install -y git build-essential automake && \  
git clone https://github.com/Parchive/par2cmdline.git && \  
cd par2cmdline && \  
aclocal && \  
automake --add-missing && \  
autoconf && \  
./configure && \  
make && \  
make check && \  
make install && \  
cd /data && \  
rm -rf par2cmdline && \  
apt-get remove -y git build-essential automake && \  
apt-get autoremove -y && \  
apt-get purge  
  

