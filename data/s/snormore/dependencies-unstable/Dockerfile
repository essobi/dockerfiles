FROM ubuntu  
  
MAINTAINER SkyDB skydb.io  
  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >
/etc/apt/sources.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu precise-updates universe' >>
/etc/apt/sources.list && \  
apt-get update  
  
#Prevent daemon start during install  
RUN dpkg-divert --local \--rename --add /sbin/initctl && ln -s /bin/true
/sbin/initctl  
  
#Utilities  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential vim less
curl git wget  
  
RUN mkdir -p /usr/local/src  
  
# golang  
RUN cd /usr/local/src && \  
wget https://go.googlecode.com/files/go1.2.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.2.linux-amd64.tar.gz  
  
ENV PATH $PATH:/usr/local/go/bin  
  
# LLVM  
RUN cd /usr/local/src && \  
wget http://llvm.org/releases/3.2/llvm-3.2.src.tar.gz && \  
tar zxvf llvm-3.2.src.tar.gz && \  
cd llvm-3.2.src && \  
./configure --enable-optimized && \  
REQUIRES_RTTI=1 make install  
  
# LMDB  
RUN cd /usr/local/src && \  
wget -O lmdb-master.tar.gz https://github.com/skydb/lmdb/archive/master.tar.gz
&& \  
tar zxvf lmdb-master.tar.gz && \  
cd lmdb-master && \  
make && \  
PREFIX=/usr/local make install  
  

