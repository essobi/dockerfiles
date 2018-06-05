FROM openuniversity/data-analysis  
  
###  
# GIS Stuff  
###  
RUN apt-get update && apt-get install -y -q \  
gdal-bin \  
libgdal-dev \  
python-gdal \  
python3-gdal  
  
#RUN pip2 install GDAL  
#RUN pip3 install GDAL  
RUN pip2 install shapely  
RUN pip3 install shapely  
  
RUN pip2 install fiona  
RUN pip3 install fiona  
  
RUN pip2 install descartes  
RUN pip3 install descartes  
  
RUN pip2 install pysal  
RUN pip3 install pysal  
  
# Install GeoPy for Geolocation  
RUN pip2 install geopy  
RUN pip3 install geopy  
  

