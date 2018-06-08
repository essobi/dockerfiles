FROM continuumio/anaconda  
  
RUN mkdir -p /code  
WORKDIR /code  
  
RUN apt-get update && apt-get install -yy \  
build-essential \  
git  
  
RUN git clone https://github.com/UDST/pandana.git  
RUN cd pandana && python setup.py install  

