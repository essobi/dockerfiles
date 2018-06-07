FROM heres/centos7-systemd  
MAINTAINER "Łukasz Kaczynski" <lukasz.kaczynski@devsoft.pl>  
  
ENV PATH /usr/local/bin:$PATH  
  
RUN yum -y update && \  
yum groupinstall -y development && \  
yum install -y \  
bzip2-devel \  
git \  
hostname \  
openssl \  
openssl-devel \  
sudo \  
tar \  
wget \  
zlib-dev  
  
RUN cd /tmp && \  
wget https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz && \  
tar xvfz Python-2.7.11.tgz && \  
cd Python-2.7.11 && \  
./configure --prefix=/usr/local && \  
make && \  
make altinstall && \  
rm -rf Python-2.7.11.tgz Python-2.7.11  
  
# Install setuptools + pip  
RUN cd /tmp && \  
wget --no-check-certificate
https://pypi.python.org/packages/source/s/setuptools/setuptools-20.1.1.tar.gz
&& \  
tar -xvf setuptools-20.1.1.tar.gz && \  
cd setuptools-20.1.1 && \  
python2.7 setup.py install && \  
curl https://bootstrap.pypa.io/get-pip.py | python2.7 && \  
rm -rf setuptools-20.1.1.tar.gz setuptools-20.1.1  
  
# Install GEOS  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh epel-release-latest-7*.rpm  
  
RUN yum --enablerepo epel install -y geos proj  
  
# Install uwsgi  
RUN pip install uwsgi  
  
# Install pgsql support  
RUN yum install -y postgresql postgresql-devel  
RUN pip install mercurial  
RUN pip install psycopg2  
  

