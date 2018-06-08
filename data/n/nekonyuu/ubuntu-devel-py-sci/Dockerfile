FROM nekonyuu/ubuntu-devel:trusty  
MAINTAINER Jonathan Raffre <nk@nyuu.eu>  
  
# prepare system environment  
RUN apt-add-repository -y ppa:ubuntugis/ubuntugis-unstable \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
python-dev \  
python-pip \  
g++ \  
gcc \  
libblas-dev \  
liblapack-dev \  
gfortran \  
libgdal-dev=1.11.2+dfsg-1~exp2~trusty \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install pip modules  
RUN C_INCLUDE_PATH=/usr/include/gdal CPLUS_INCLUDE_PATH=/usr/include/gdal pip
install pandas==0.15.2 statsmodels==0.6.1 gdal==1.11.2 numpy==1.9.2
scipy==0.16.1 && rm -rf /root/.cache/pip/  

