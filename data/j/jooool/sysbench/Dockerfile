# /!\ DOES NOT WORK UNTIL PRIVILEGED MODE AVAILABLE IN DOCKERFILE  
  
FROM centos:6.9  
LABEL maintainer=jooool  
  
# Update APT base then install mpc-batch dependencies  
RUN yum install -y automake libtool && \  
mkdir -p /root/sysbench/src && \  
cd /root/sysbench/src && \  
wget https://github.com/akopytov/sysbench/archive/1.0.12.tar.gz && \  
rm sysbench-1.0.12 -rf && \  
tar xf sysbench-1.0.12.tar.gz && \  
cd sysbench-1.0.12 && \  
./autogen.sh && \  
./configure --without-mysql --with-extra-ldflags=-all-static && \  
make && \  
make install

