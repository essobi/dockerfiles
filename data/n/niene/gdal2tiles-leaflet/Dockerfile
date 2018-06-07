## GDAL2Tiles  
## Builds gdal2tiles on gdal  
FROM geodata/gdal  
MAINTAINER Niene Boeijen <niene@webmapper.net>  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y --fix-missing\  
wget \  
unzip \  
python \  
python-gdal  
  
WORKDIR /master  
  
RUN wget https://github.com/commenthol/gdal2tiles-leaflet/archive/master.zip
&& \  
unzip master.zip  
  
WORKDIR /master/gdal2tiles-leaflet-master  
  
ENTRYPOINT ["./gdal2tiles.py"]

