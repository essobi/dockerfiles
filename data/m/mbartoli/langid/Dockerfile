FROM ubuntu:14.04  
MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"  
RUN apt-get update && apt-get install -y build-essential \  
python \  
python-dev \  
python-setuptools \  
python-numpy \  
git  
  
WORKDIR /home  
RUN git clone https://github.com/saffsd/langid.py  
  
WORKDIR /home/langid.py  
RUN python setup.py build  
RUN python setup.py install  
  
WORKDIR /home/langid.py/langid  
#RUN python langid.py -s  

