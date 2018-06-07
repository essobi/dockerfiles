FROM centos:7  
MAINTAINER domeos  
  
ENV GCC_VERSION 4.9.0  
WORKDIR /opt  
  
RUN yum -y install wget bzip2 && \  
yum -y install gcc gcc-c++ gdb make && \  
wget http://ftp.gnu.org/gnu/gcc/gcc-${GCC_VERSION}/gcc-${GCC_VERSION}.tar.bz2
&& \  
tar -jxvf gcc-${GCC_VERSION}.tar.bz2 && \  
cd gcc-${GCC_VERSION} && \  
./contrib/download_prerequisites && cd .. && \  
mkdir gcc-build-${GCC_VERSION} && cd gcc-build-${GCC_VERSION} && \  
../gcc-${GCC_VERSION}/configure --enable-checking=release --enable-
languages=c,c++ --disable-multilib && \  
make -j4 && \  
make install && \  
rm -rf /opt/gcc-build-${GCC_VERSION}/ && \  
rm -rf /opt/gcc-${GCC_VERSION}/ && \  
rm -rf /opt/gcc-${GCC_VERSION}.tar.gz  

