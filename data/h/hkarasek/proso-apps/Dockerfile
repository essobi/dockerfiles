FROM ubuntu:xenial  
MAINTAINER xkarase1@fi.muni.cz  
  
RUN apt-get update && apt-get install -y apt-utils && apt-get install -y
build-essential wget python3-dev libblas-dev liblapack-dev gfortran git
python3-pip libfreetype6-dev python3-matplotlib libpq-dev postgresql-client  
RUN ln -s /usr/bin/pip3 /usr/bin/pip  
RUN ln -s /usr/bin/python3 /usr/bin/python  
RUN pip install --upgrade pip  
RUN pip install setuptools  
RUN pip install -U Sphinx  
RUN pip install -U sphinxcontrib-napoleon>=0.5.0  
  
# instalace závislostí pomocí make  
RUN git clone https://github.com/adaptive-learning/proso-apps.git && cd proso-
apps && make install  
RUN rm -rf /proso-apps  
  
RUN mkdir /proso-apps

