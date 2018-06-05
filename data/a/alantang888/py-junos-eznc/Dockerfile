FROM centos:7  
MAINTAINER Alan Tang  
  
RUN yum -y groupinstall "Development Tools" && \  
yum install -y openssl-devel python-setuptools python-devel libxml2-devel
libxslt-devel net-snmp-devel libffi-devel && \  
easy_install pip && \  
pip install easysnmp ZODB cryptography junos-eznc  
  
WORKDIR /root  
  
COPY program.py .  
  
CMD python program.py  

