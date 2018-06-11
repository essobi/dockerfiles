FROM ogrisel/distributed:latest  
MAINTAINER Sergiy Savchuk  
  
RUN apt-get update -yqq && apt-get -yqq install \  
wget \  
liblz4-tool \  
build-essential  
  
# Install arctic  
RUN pip install --upgrade pip; pip install six Cython qpython  
RUN pip install git+https://github.com/manahl/arctic.git  
  
# Add ArcticMisc  
COPY ArcticMisc ArcticMisc  
RUN cd ArcticMisc; python setup.py install; cd ..  
  

