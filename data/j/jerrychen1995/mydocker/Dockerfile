# shadowsocks  
FROM ubuntu:16.04  
MAINTAINER jerusalemc <528122401@qq.com>  
##  
RUN apt-get update && \  
apt-get install -y python-gevent python-pip python-m2crypto python-wheel
python-setuptools  
RUN pip install shadowsocks  
  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/local/bin/ssserver"]  
  

