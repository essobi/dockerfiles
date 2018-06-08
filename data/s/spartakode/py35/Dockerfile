FROM ubuntu:14.04.2  
MAINTAINER Adnan Issadeen <adnan.issadeen@live.com>  
  
RUN apt-get update && apt-get install wget curl sqlite3 vim -y --force-yes  
RUN apt-get update && apt-get -y --force-yes build-dep python3.4  
RUN mkdir /usr/src/python  
WORKDIR /usr/src/python  
RUN wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz \  
&& tar -xvf Python-3.5.0.tgz  
WORKDIR /usr/src/python/Python-3.5.0  
RUN ./configure \  
&& make -j$(nproc) \  
&& make altinstall  

