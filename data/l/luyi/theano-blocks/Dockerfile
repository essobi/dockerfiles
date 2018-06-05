FROM ubuntu:14.04  
MAINTAINER luyi  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
RUN apt-get update  
  
RUN apt-get install -y python3-dev python3-setuptools python3-h5py
python3-numpy python3-scipy libhdf5-dev git  
  
RUN easy_install3 pip  
  
RUN pip3 install git+git://github.com/mila-udem/blocks.git@stable -r
https://raw.githubusercontent.com/mila-udem/blocks/stable/requirements.txt  
  
RUN git clone https://github.com/mila-udem/picklable-itertools.git  
  
RUN python3 picklable-itertools/setup.py install  
  
RUN rm -rf picklable-itertools  

