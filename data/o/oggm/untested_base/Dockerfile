###################################################  
# Dockerfile to build a Python 3.6 environment  
# with OGGM installed, based on Ubuntu 17.10.  
###################################################  
FROM ubuntu:17.10  
MAINTAINER Timo Rothenpieler  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get -y install \  
gfortran \  
fontconfig \  
fonts-dejavu \  
git \  
build-essential \  
liblapack-dev \  
libproj-dev \  
libfreetype6-dev \  
gdal-bin \  
libgdal-dev \  
libagg-dev \  
liblapack-dev \  
netcdf-bin \  
libnetcdf-dev \  
python3.6-dev \  
python3.6 \  
python3-pip \  
locales && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV PIP python3.6 -m pip  
  
RUN \  
$PIP install --no-cache-dir --upgrade "pip<10" setuptools  
  
RUN \  
$PIP install --no-cache-dir --upgrade numpy && \  
$PIP install --no-cache-dir --upgrade scipy && \  
$PIP install --no-cache-dir --upgrade pandas shapely cython  
  
RUN \  
$PIP install --no-cache-dir --no-binary matplotlib --upgrade matplotlib  
  
RUN \  
$PIP install --no-cache-dir --upgrade "gdal==2.2.1" \--install-
option="build_ext" \--install-option="--include-dirs=/usr/include/gdal"  
  
RUN \  
$PIP install --no-cache-dir --upgrade fiona --install-option="build_ext"
\--install-option="--include-dirs=/usr/include/gdal"  
  
RUN \  
$PIP install --no-cache-dir --upgrade pyproj rasterio Pillow geopandas
"netcdf4<1.4" scikit-image configobj joblib xarray cartopy nose filelock
pytest pytest-mpl pytest-cov pytest-xdist ilock progressbar2 boto3 motionless
versioneer  
  
RUN \  
$PIP install --no-cache-dir --upgrade
git+https://github.com/fmaussion/salem.git@eeab83d4b78430a3eea2bdc83c426ae6e5806ece  
  
RUN \  
sed -i 's/^backend.*/backend : Agg/' /usr/local/lib/python3.6/dist-
packages/matplotlib/mpl-data/matplotlibrc && \  
sed -i "s/python3$/python3.6/g" "$(which pip3)" && \  
cd /usr/bin && \  
rm python3 && \  
ln -s python3.6 python3  
  
RUN python3.6 -c "import matplotlib.font_manager, salem"  
  
RUN sed -i "s/python3$/python3.6/g" /usr/bin/pip3  
  
ADD test.sh /root/test.sh  

