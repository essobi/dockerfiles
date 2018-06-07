FROM ubuntu:15.04  
MAINTAINER Jacques Tardie <hi@jacquestardie.org>  
  
# Install dependencies.  
RUN apt-get update && apt-get install -y \  
pkg-config \  
wget \  
git \  
libpng12-0 \  
libfreetype6-dev \  
python \  
python-pycurl \  
python-pip \  
python-numpy \  
libgdal-dev \  
libatlas-base-dev \  
gfortran \  
python-scipy  
  
# Set the locale.  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# See: https://stackoverflow.com/questions/27341064/how-do-i-fix-importerror-
cannot-import-name-incompleteread  
RUN easy_install -U pip  
  
# Install landsat-util.  
RUN pip install landsat-util  
  
# Set the primary command to 'landsat'  
# Allows the image to be run as `docker run landsat`  
ENTRYPOINT ["landsat"]  
CMD ["--help"]  

