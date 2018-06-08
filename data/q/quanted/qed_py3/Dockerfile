# from latest official python 3 docker build  
# debian linux with buildpack-deps  
FROM python:3  
# Set working directory to src to run commands  
WORKDIR /src  
# Set versions for GIS Packages  
ENV GEOS_VERSION=3.6.2  
ENV GDAL_VERSION=2.2.1  
ENV PROJ4_VERSION=5.0.1  
  
# Install GEOS  
RUN wget http://download.osgeo.org/geos/geos-${GEOS_VERSION}.tar.bz2 -O
/tmp/geos-${GEOS_VERSION}.tar.bz2 \  
&& tar -xf /tmp/geos-${GEOS_VERSION}.tar.bz2 -C /tmp \  
&& cd /tmp/geos-${GEOS_VERSION} \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /tmp/geos-${GEOS_VERSION}  
  
# Install GDAL  
RUN wget
http://download.osgeo.org/gdal/$GDAL_VERSION/gdal-${GDAL_VERSION}.tar.gz -O
/tmp/gdal-${GDAL_VERSION}.tar.gz \  
&& tar -x -f /tmp/gdal-${GDAL_VERSION}.tar.gz -C /tmp \  
&& cd /tmp/gdal-${GDAL_VERSION} \  
&& ./configure \  
\--prefix=/usr \  
\--with-python \  
\--with-geos \  
\--with-sfcgal \  
\--with-geotiff \  
\--with-jpeg \  
\--with-png \  
\--with-expat \  
\--with-libkml \  
\--with-openjpeg \  
\--with-pg \  
\--with-curl \  
\--with-spatialite \  
&& make -j $(nproc) \  
&& make install \  
&& rm /tmp/gdal-${GDAL_VERSION} -rf  
  
# Install Proj.4  
RUN wget \--no-check-certificate \--content-disposition
https://github.com/OSGeo/proj.4/releases/download/${PROJ4_VERSION}/proj-${PROJ4_VERSION}.tar.gz
-O /tmp/proj-${PROJ4_VERSION}.tar.gz \  
&& tar -xvf /tmp/proj-${PROJ4_VERSION}.tar.gz -C /tmp \  
&& cd /tmp/proj-${PROJ4_VERSION} \  
&& ./configure \--prefix=/usr \  
&& make \  
&& make install \  
&& rm -rf /tmp/proj-${PROJ4_VERSION}  
  
#Add requirements file before install requirements  
COPY requirements_qed/requirements.txt ./requirements.txt  
#Install requirements, including nose2  
RUN pip install -r requirements.txt  

