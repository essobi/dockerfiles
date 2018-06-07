FROM amazonlinux:latest  
  
RUN yum -y update && \  
yum -y install \  
gcc \  
gcc-c++ \  
make \  
zlib-devel \  
bzip2-devel \  
openssl-devel \  
readline-devel \  
ncurses-devel \  
sqlite-devel && \  
curl --remote-name --progress
https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz && \  
echo '2d0fc9f3a5940707590e07f03ecb08b9 Python-3.6.1.tgz' | md5sum -c - && \  
tar zxf Python-3.6.1.tgz && \  
cd Python-3.6.1 && \  
./configure --prefix=/usr/local --enable-shared && \  
make && \  
make altinstall && \  
echo '/usr/local/lib' > /etc/ld.so.conf.d/local-libs.conf && \  
ldconfig && \  
cd .. && \  
rm -rf Python-3.6.1.tgz Python-3.6.1  

