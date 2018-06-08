FROM centos:7  
  
RUN yum -y install libtool openssl-devel libxml2-devel boost-devel gcc gcc-c++
wget make automake && \  
wget
http://wpfilebase.s3.amazonaws.com/torque/torque-6.0.2-1469811694_d9a3483.tar.gz
-O torque.tar.gz && \  
tar -xzvf torque.tar.gz && \  
cd torque-* && \  
./configure && \  
make && make install && \  
cd .. && \  
rm -rf torque* && \  
yum remove -y libtool openssl-devel libxml2-devel boost-devel gcc gcc-c++ wget
make automake && \  
yum clean all  

