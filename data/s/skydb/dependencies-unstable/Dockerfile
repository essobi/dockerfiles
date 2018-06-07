FROM ubuntu  
  
MAINTAINER Sky Contributors skydb.io  
  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >
/etc/apt/sources.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu precise-updates universe' >>
/etc/apt/sources.list && \  
apt-get update  
  
# Prevent daemon start during install  
RUN dpkg-divert --local \--rename --add /sbin/initctl && ln -s /bin/true
/sbin/initctl  
  
# Utilities  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential vim less
curl git wget  
  
RUN mkdir -p /usr/local/src  
  
# Go 1.2  
RUN cd /usr/local/src && \  
wget https://go.googlecode.com/files/go1.2.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.2.linux-amd64.tar.gz  
  
ENV PATH $PATH:/usr/local/go/bin  
  
# LMDB 0.9.11  
RUN cd /usr/local/src && \  
wget https://github.com/skydb/dependencies/raw/unstable/lmdb.tar.gz && \  
tar zxvf lmdb.tar.gz && \  
cd lmdb && \  
make && \  
PREFIX=/usr/local make install  
  
# LLVM  
RUN cd /usr/local/src && \  
wget http://llvm.org/releases/3.4/llvm-3.4.src.tar.gz && \  
tar zxvf llvm-3.4.src.tar.gz && \  
cd llvm-3.4 && \  
./configure --enable-optimized --enable-shared && \  
REQUIRES_RTTI=1 make install  
  

