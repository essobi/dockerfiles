FROM python:3.6  
LABEL maintainer="Joe Cridge <joe.cridge@me.com>" version="0.1.0"  
# Install geospatial libraries.  
RUN apt-get -y update && \  
apt-get -y install binutils libproj-dev gdal-bin  
  
# Install zip.  
RUN apt-get -y install zip  
  
# Install AWS CLI.  
RUN pip install awscli  

