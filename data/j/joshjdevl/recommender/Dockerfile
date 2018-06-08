FROM ubuntu:precise  
MAINTAINER joshjdevl < joshjdevl [at] gmail {dot} com>  
  
RUN apt-get update && apt-get -y install python-software-properties software-
properties-common  
RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc) universe"  
RUN apt-get update  
  
RUN add-apt-repository ppa:apt-fast/stable  
RUN apt-get update  
RUN apt-get -y install apt-fast  
  
RUN apt-fast -y install wget  
RUN apt-fast update  
  
RUN apt-fast -y install gcc g++ build-essential libopenmpi-dev openmpi-bin
default-jdk cmake zlib1g-dev git vim  
RUN apt-fast install -y autoconf autoconf automake build-essential autogen
libtool  
RUN apt-fast install -y zlib1g-dev libssl-dev libbz2-dev libsqlite3-dev  
RUN apt-fast -y install python-dev python-pip  
  
RUN apt-fast -y install python-dev python-numpy python-numpy-dev python-
setuptools python-numpy-dev python-scipy libatlas-dev g++  
RUN pip install -U scikits.learn  
RUN apt-fast -y install python-matplotlib  
#RUN pip install -U crab  
RUN cd /tmp && git clone https://github.com/muricoca/crab  
RUN cd /tmp/crab && python setup.py install  

