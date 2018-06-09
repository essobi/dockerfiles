FROM centos:7  
RUN yum update -y && yum clean all  
  
RUN yum install -y \  
autoconf \  
automake \  
bison \  
boost \  
boost-devel \  
flex \  
gcc-c++ \  
gcc \  
git \  
glib2 \  
glib2-devel \  
libtool \  
m4 \  
make \  
openssl \  
openssl-devel \  
pkgconfig \  
python \  
python-devel \  
tar \  
unzip \  
wget  
  
RUN curl https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install --upgrade Twisted setuptools  
  
ADD . /tmp/thrift  
RUN cd /tmp/thrift && \  
./bootstrap.sh && \  
PY_PREFIX=/usr/local ./configure --prefix=/usr/local && \  
make && \  
make install && \  
cd /tmp && \  
rm -rf /tmp/thrift  
  
RUN echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf && \  
ldconfig -v  
  
RUN echo '/usr/local/lib64/python2.7/site-packages' >
/usr/lib64/python2.7/site-packages/local.pth  

