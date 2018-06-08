FROM ubuntu:trusty  
  
MAINTAINER Omixy Ltd. <tech@omixy.com>  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# Necessary to use add-apt-repository  
RUN apt-get update && apt-get install -y software-properties-common  
  
# This repo contains different versions of Python  
RUN add-apt-repository -y ppa:fkrull/deadsnakes;  
  
RUN apt-get update && apt-get install -y \  
python3-pip \  
python3.4 \  
python3.4-dev \  
python3.5 \  
python3.5-dev \  
build-essential \  
libpq-dev;  
  
CMD ["python"]  

