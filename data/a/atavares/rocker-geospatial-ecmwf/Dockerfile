FROM rocker/geospatial:latest  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
python \  
python-pip \  
curl \  
libxml2-dev \  
libcurl4-openssl-dev \  
libboost-dev  
  
RUN pip install
https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-
client-python.tgz  
  
RUN install2.r --error \  
reticulate \  
GEOmap \  
selectr  
  

