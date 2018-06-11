# Python  
#  
# Base: centos7  
FROM centos:centos7  
MAINTAINER Andrew Cutler <andrew@panubo.com>  
  
# 1. Update & Install  
# 2. Required for virtualenv bootstrap / install  
# 3. Base packages required for compiling popular Python packages  
# 4. Base packages for compiling Python  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \  
yum -q -y update && \  
yum -q -y install curl mercurial git tar bzip2 python-jinja2 && \  
yum -q -y install gcc freetype ghostscript freetype-devel libpng libjpeg-turbo
libpng-devel libjpeg-turbo-devel python-devel libxml2-devel libxslt-devel
mariadb-devel && \  
yum -q -y install make openssl-devel sqlite-devel libffi-devel bzip2-devel &&
\  
yum -q clean all  
  
# Compile & Install Python from source  
RUN for PYTHON in 2.7.13 3.3.7 3.4.7 3.5.4 3.6.4; do mkdir -p /tmp/build && cd
/tmp/build && curl -O
https://www.python.org/ftp/python/${PYTHON}/Python-${PYTHON}.tgz && tar -xzf
Python-${PYTHON}.tgz && \  
cd /tmp/build/Python-${PYTHON} && ./configure && make -j `nproc` && make
install && rm -rf /tmp/build/Python-${PYTHON}; done  
  
# Clean up  
RUN rm -rf /tmp/* /tmp/build/ /var/tmp/* && \  
# Remove links to indefinite Python versions (also prevents os Python from
being overridden by accident)  
find /usr/local/bin/ -type l -exec rm {} \; && \  
rm -rf /var/cache/yum/*  

