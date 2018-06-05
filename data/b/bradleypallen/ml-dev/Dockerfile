################################################################################  
# Dockerfile to build an image for training and evaluating classification  
# and prediction models using Vowpal Wabbit and perf  
# Based on Ubuntu  
################################################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:latest  
  
# File Author / Maintainer  
MAINTAINER Bradley P. Allen "bradley.p.allen@gmail.com"  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install VW build prerequisites  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install build-essential  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install automake  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install autoconf  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install libxmu-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install gcc  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install libpthread-stubs0-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install libtool  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install libboost-program-
options-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install libboost-python-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install zlib1g-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install libc6  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install libgcc1  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install libstdc++6  
  
# Install Python tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-pip  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-setuptools  
RUN pip install --upgrade pip  
RUN pip install --upgrade virtualenv  
RUN pip install --upgrade fabric  
  
# Install other tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q emacs  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q git  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q wget  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q curl  
  
# Install ml_dev  
RUN cd /home;git clone https://github.com/bradleypallen/ml_dev.git  
  
# Add /usr/local/lib to LD_LIBRARY_PATH  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib  
  
# Install and make vw (Vowpal Wabbit) and perf  
RUN cd /usr/local/src;git clone
https://github.com/bradleypallen/vowpal_wabbit.git;cd
vowpal_wabbit;./autogen.sh;./configure;make;make test;make install  
RUN cd /usr/local/src;wget
http://osmot.cs.cornell.edu/kddcup/perf/perf.src.tar.gz;tar xvf
perf.src.tar.gz;rm perf.src.tar.gz;mv perf.src perf;cd perf;make -B perf;make
install  

