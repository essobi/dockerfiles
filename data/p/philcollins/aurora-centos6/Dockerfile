# Latest version of centos  
FROM centos:centos6  
  
MAINTAINER Steve Salevan <steve.salevan@gmail.com>  
  
RUN yum -y update && \  
yum groupinstall -y development && \  
yum -y install epel-release && \  
yum install -y \  
bzip2-devel \  
cyrus-sasl-libs \  
git \  
hostname \  
openssl \  
openssl-devel \  
sqlite-devel \  
sudo \  
tar \  
wget \  
zlib-dev  
  
RUN cd /tmp && \  
wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz && \  
tar xvfz Python-2.7.8.tgz && \  
cd Python-2.7.8 && \  
./configure --enable-shared --prefix=/usr && \  
make && \  
make altinstall  
  
RUN bash -c 'ln -s /usr/lib/libpython* /usr/lib64'  
  
# Install setuptools + pip  
RUN cd /tmp && \  
wget --no-check-certificate
https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz
&& \  
tar -xvf setuptools-1.4.2.tar.gz && \  
cd setuptools-1.4.2 && \  
python2.7 setup.py install && \  
curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py |
python2.7 - && \  
pip install virtualenv  

