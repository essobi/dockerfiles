FROM centos:centos7  
  
USER root  
  
# Perform updates  
RUN yum -y update; yum clean all  
  
# Install EPEL & Dependencies  
RUN yum -y install epel-release && yum repolist && \  
yum install -y git wget zlib-devel bzip2-devel xz-devel libcurl-devel openssl-
devel && \  
yum -y group install "Development Tools"  
  
# Install software  
RUN wget
https://github.com/samtools/htslib/releases/download/1.6/htslib-1.6.tar.bz2 &&
\  
git clone https://github.com/CRUKMI-ComputationalBiology/bamcmp.git && \  
bunzip2 htslib-1.6.tar.bz2 && tar xvf htslib-1.6.tar && \  
cd /htslib-1.6 && ./configure && make && make install  
ENV LD_LIBRARY_PATH=/usr/local/lib  
RUN cd /bamcmp && make && cp /bamcmp/build/bamcmp /usr/local/bin/  
ENTRYPOINT bamcmp  

