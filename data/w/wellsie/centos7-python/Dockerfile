FROM wellsie/centos7  
MAINTAINER Jono Wells <_oj.io>  
  
# setup a reasonable Python environment with libevent support  
RUN yum -y install \  
gcc \  
libevent-devel\  
python-backports-lzma \  
python-devel \  
python-pip && \  
yum -y clean all  

