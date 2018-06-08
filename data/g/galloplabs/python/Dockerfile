FROM ubuntu:14.04  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
RUN apt-get update && apt-get -y upgrade && apt-get install -y build-essential
python python-dev libpq-dev libssl-dev libffi-dev zlib1g-dev git  
  
ADD https://raw.github.com/pypa/pip/master/contrib/get-pip.py get-pip.py  
RUN python get-pip.py  
RUN pip install \--upgrade pip  
  
RUN pip install requests[security]==2.8.0  
RUN pip install virtualenv  

