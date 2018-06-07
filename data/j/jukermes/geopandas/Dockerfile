FROM tailordev/pandas  
  
MAINTAINER Julien Kermes <julien.kermes@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y binutils libproj-dev gdal-bin  
  
RUN mkdir -p /opt/geopandas/build/  
  
COPY requirements.txt /opt/geopandas/build/requirements.txt  
  
RUN pip install --upgrade pip  
  
RUN pip install -r /opt/geopandas/build/requirements.txt

