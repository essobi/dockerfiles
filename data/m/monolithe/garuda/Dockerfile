# Garuda  
#  
# Version 0.0.1  
FROM python:2.7  
MAINTAINER Antoine Mercadal <antoine@nuagenetworks.net>  
LABEL Description="This image can be used as a base image for all Garuda based
applications." Version="0.0.1"  
  
ADD . /install  
  
RUN cd /install && \  
pip install -r requirements.txt && \  
python setup.py install

