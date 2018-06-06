FROM ubuntu:xenial  
  
# install python and gdal packages  
RUN apt-get update && apt-get install -y\  
git\  
vim\  
python \  
ipython\  
build-essential\  
python-software-properties\  
software-properties-common\  
python-pip\  
python-scipy\  
python-dev\  
gdal-bin\  
python-gdal\  
libgdal-dev  
  
# install ml dependencies  
RUN pip install gdal numpy ephem psycopg2  
RUN pip install git+https://github.com/DigitalGlobe/mltools  
  
# put code into image  
ADD ./bin /  

