FROM centos:6.6  
MAINTAINER Ryan Liao <pirsquare.ryan@gmail.com>  
  
ENV PATH="/usr/local/bin:$PATH"  
RUN yum -y update; \  
yum install -y zlib-devel openssl-devel sqlite-devel bzip2-devel wget tar xz
xz-libs sudo \  
gcc gcc-g++ git make libselinux-python python-argparse  
  
WORKDIR /tmp  
  
RUN wget http://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz; \  
xz -d Python-2.7.9.tar.xz && tar -xvf Python-2.7.9.tar && cd Python-2.7.9 \  
&& ./configure --prefix=/usr/local \--enable-unicode=ucs4 --enable-shared \  
&& make && make altinstall  
  
RUN echo '/usr/local/lib' >> '/etc/ld.so.conf' && ldconfig  
  
WORKDIR /tmp  
  
RUN wget --no-check-certificate
https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz;
\  
tar -xvf setuptools-1.4.2.tar.gz  
  
WORKDIR setuptools-1.4.2  
  
RUN python2.6 setup.py install; python2.7 setup.py install  
  
RUN easy_install-2.6 pip; easy_install-2.7 pip  
  

