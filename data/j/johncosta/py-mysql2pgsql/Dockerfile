FROM ubuntu:12.04  
RUN apt-get update  
RUN apt-get install -y wget ca-certificates python-dev \  
libpq-dev libmysqlclient-dev python-setuptools  
  
# install py-mysql2pgsql  
ADD . /build  
RUN cd /build && python setup.py install && rm -rf /build  

