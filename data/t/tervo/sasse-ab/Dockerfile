# Initial version of SASSE docker file. For now, tested only for creating
confusion matrix.  
# FROM consbio/python3.6-gdal2  
FROM python:3.6  
# Install GDAL2, taken from : https://github.com/GeographicaGS/Docker-
GDAL2/blob/master/2.2.3/Dockerfile  
ENV ROOTDIR /usr/local/  
ENV GDAL_VERSION 2.2.3  
ENV OPENJPEG_VERSION 2.2.0  
# Load assets  
WORKDIR $ROOTDIR/  
  
ADD http://download.osgeo.org/gdal/${GDAL_VERSION}/gdal-${GDAL_VERSION}.tar.gz
$ROOTDIR/src/  
ADD https://github.com/uclouvain/openjpeg/archive/v${OPENJPEG_VERSION}.tar.gz
$ROOTDIR/src/openjpeg-${OPENJPEG_VERSION}.tar.gz  
  
# Install basic dependencies  
RUN apt-get update -y && apt-get install -y \  
software-properties-common \  
python-software-properties \  
python3-software-properties \  
build-essential \  
python-dev \  
python3-dev \  
python-numpy \  
python3-numpy \  
libspatialite-dev \  
sqlite3 \  
libpq-dev \  
libcurl4-gnutls-dev \  
libproj-dev \  
libxml2-dev \  
libgeos-dev \  
libnetcdf-dev \  
libpoppler-dev \  
libspatialite-dev \  
libhdf4-alt-dev \  
libhdf5-serial-dev \  
wget \  
bash-completion \  
cmake  
  
# Compile and install OpenJPEG  
RUN cd src && tar -xvf openjpeg-${OPENJPEG_VERSION}.tar.gz && cd
openjpeg-${OPENJPEG_VERSION}/ \  
&& mkdir build && cd build \  
&& cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$ROOTDIR \  
&& make && make install && make clean \  
&& cd $ROOTDIR && rm -Rf src/openjpeg*  
  
# Compile and install GDAL  
RUN cd src && tar -xvf gdal-${GDAL_VERSION}.tar.gz && cd gdal-${GDAL_VERSION}
\  
&& ./configure --with-python --with-spatialite --with-pg --with-curl --with-
openjpeg=$ROOTDIR \  
&& make && make install && ldconfig \  
&& apt-get update -y \  
&& apt-get remove -y --purge build-essential wget \  
&& cd $ROOTDIR && cd src/gdal-${GDAL_VERSION}/swig/python \  
&& python3 setup.py build \  
&& python3 setup.py install \  
&& cd $ROOTDIR && rm -Rf src/gdal*  
# End GDAL2 install  
RUN mkdir /a  
WORKDIR /a  
  
RUN pip install matplotlib opencv-python psycopg2-binary unicodecsv SQLAlchemy
GeoAlchemy2 pyproj requests pyyaml scikit-learn scipy  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_CTYPE=C.UTF-8  
# RUN rm -rf /root/.cache/matplotlib  
# docker run --rm -v /smartdev/run/products/sasse/bin:/a sasse python xx.py  

