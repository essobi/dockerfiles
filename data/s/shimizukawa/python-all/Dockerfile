# Ubuntu latest and Python 2.4, 2.5, 2.6, 2.7, 3.1, 3.2, 3.3, 3.4, pypy  
FROM stackbrew/ubuntu:latest  
MAINTAINER Takayuki SHIMIZUKAWA "shimizukawa@gmail.com"  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe\ndeb
http://archive.ubuntu.com/ubuntu trusty-updates main universe\ndeb
http://archive.ubuntu.com/ubuntu trusty-security main universe" >
/etc/apt/sources.list  
run apt-get update && \  
apt-get install -qq -y openssl  
run apt-get update && \  
apt-get install -qq -y software-properties-common && \  
add-apt-repository ppa:fkrull/deadsnakes && \  
add-apt-repository ppa:pypy/ppa && \  
apt-get update  
RUN apt-get install -qq -y \  
python2.4 \  
python2.5 \  
python2.6 \  
python2.7 \  
python3.1 \  
python3.2 \  
python3.3 \  
python3.4 \  
pypy  
run apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  

