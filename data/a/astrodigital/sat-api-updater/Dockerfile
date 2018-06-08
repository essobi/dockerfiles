FROM ubuntu:14.04  
RUN apt-get -y update -qq  
RUN apt-get install -y libgdal1h \  
gdal-bin \  
libgdal-dev \  
libgeos-dev \  
git-core \  
python-numpy \  
python-pip \  
gfortran \  
python-pycurl \  
python-dev  
RUN pip install iron-worker>=1.3.1  
RUN mkdir -p /apps  
RUN cd /apps && git clone
https://github.com/AstroDigital/landsat8-metadata.git && \  
cd landsat8-metadata && git checkout tags/v0.4.5  
RUN cd /apps && git clone
https://github.com/AstroDigital/sentinel2-metadata.git && \  
cd sentinel2-metadata && git checkout tags/v0.4.5  
RUN pip install -r /apps/landsat8-metadata/requirements.txt  
RUN pip install -r /apps/sentinel2-metadata/requirements.txt  
RUN pip install boto  

