FROM mesoscloud/centos:7-20160605  
MAINTAINER Peter Ericson <pdericson@gmail.com>  
# install python3 and kazoo, compile haproxy  
RUN HAPROXY_VERSION=1.5.14; \  
\  
yum install -y epel-release && \  
yum install -y gcc make openssl-devel pcre-devel python34 && \  
yum clean all && \  
\  
curl -fLO https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py && \  
\  
pip3 install kazoo && \  
\  
curl -fL
http://www.haproxy.org/download/1.5/src/haproxy-$HAPROXY_VERSION.tar.gz | tar
xzf \- -C /usr/src && \  
make -C /usr/src/haproxy-$HAPROXY_VERSION TARGET=linux2628 USE_PCRE=1
USE_OPENSSL=1 USE_ZLIB=1 && \  
make -C /usr/src/haproxy-$HAPROXY_VERSION install && \  
rm -rf /usr/src/haproxy-$HAPROXY_VERSION  
  
COPY init.py /init.py  
  
CMD ["python3", "-u", "/init.py"]  

