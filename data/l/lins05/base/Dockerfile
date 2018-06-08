FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV MAINTAINER linshuai2012@gmail.com  
  
# install python  
RUN apt-get update -qq  
RUN apt-get install -qy git vim curl wget telnet netcat  
RUN apt-get install -qy \  
netbase ca-certificates apt-transport-https \  
build-essential python python-dev \  
libxml2-dev libssl-dev libxslt1-dev \  
libmysqlclient-dev \  
libevent-dev \  
libffi-dev libssl-dev \  
libpcre3-dev libz-dev  
  
# install pip/wheel  
ADD https://raw.github.com/pypa/pip/master/contrib/get-pip.py /get-pip.py  
RUN python /get-pip.py  
RUN pip install -U wheel  

