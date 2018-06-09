FROM ubuntu:16.04  
WORKDIR /NGStools/  
  
#Install dependencies  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y python-dev  
RUN apt-get install -y wget  
  
#Cloning from github  
RUN git clone -b base_quality_filter https://github.com/B-UMMI/ReMatCh.git  
  
ENV PATH="/NGStools/ReMatCh:${PATH}"  
CMD rematch.py --help

