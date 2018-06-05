FROM geodata/gdal:2.1.1  
  
USER root  
  
RUN apt-get update  
  
RUN apt-get install -y --no-install-recommends \  
build-essential python-dev gcc g++ \  
python-pip postgresql libpq-dev libffi-dev libssl-dev  
  
# RUN apt-get install -y --no-install-recommends \  
# gdal-bin python-gdal libgdal1-dev \  
RUN apt-get install -y --no-install-recommends \  
libopencv-dev python-opencv python-scipy  
  
ADD ./requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
# Fails without Cython installed.  
RUN pip install scikit-image  

