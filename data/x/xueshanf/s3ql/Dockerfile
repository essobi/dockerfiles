FROM ubuntu:14.04  
MAINTAINER Xueshan Feng <xueshan.feng@gmail.com>  
  
# Update package cache  
RUN apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget  
ENV VERSION s3ql-2.15  
# Dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3
python3-setuptools python3-dev python3-pip pkg-config  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y sqlite3 libsqlite3-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-apsw
python3.4-llfuse  
RUN pip3 install defusedxml dugong requests pycrypto  
  
# This module doesn't exist in ubuntu:14:04 default repo. Get it from
bitbucket.  
RUN wget -nv -O /usr/src/${VERSION}.tar.bz2
https://bitbucket.org/nikratio/s3ql/downloads/${VERSION}.tar.bz2  
RUN tar xvj -C /usr/src -f /usr/src/${VERSION}.tar.bz2  
WORKDIR /usr/src/${VERSION}  
RUN python3 setup.py build_ext --inplace  
RUN python3 setup.py install  
  
# Add credentials  
ADD authinfo2 /root/.s3ql/authinfo2  
RUN chmod 600 /root/.s3ql/authinfo2  
  
WORKDIR /  
CMD ["/bin/bash"]  

