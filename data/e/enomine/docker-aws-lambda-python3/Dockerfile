FROM amazonlinux:latest  
  
RUN yum update -y  
  
RUN yum install -y \  
gcc \  
gcc-c++ \  
yum-utils \  
findutils \  
openssl-devel \  
zip  
  
RUN yum -y groupinstall development  
  
RUN curl https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz | tar -xJ
\  
&& cd Python-3.6.1 \  
&& ./configure --prefix=/usr/local \--enable-shared \  
&& make \  
&& make install \  
&& echo '/usr/local/lib' > /etc/ld.so.conf.d/local-libs.conf \  
&& ldconfig \  
&& cd .. \  
&& rm -rf Python-3.6.1  
  
RUN pip3 install -U pip wheel awscli --no-cache-dir  

