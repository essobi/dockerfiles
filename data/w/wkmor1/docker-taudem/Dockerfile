FROM ubuntu:14.04  
MAINTAINER William K. Morris <>  
  
ENV GDAL_VERSION 2.1.0  
ENV OPEN_MPI_SHORT_VERSION 1.8  
ENV OPEN_MPI_VERSION 1.8.1  
ENV TAUDEM_VERSION 5.3.8  
RUN apt-get update && apt-get install -y \  
build-essential \  
g++ \  
gfortran \  
python-all-dev \  
python-pip \  
python-numpy \  
libblas-dev \  
liblapack-dev \  
libgeos-dev \  
libproj-dev \  
libspatialite-dev \  
libspatialite5 \  
spatialite-bin \  
libibnetdisc-dev \  
wget \  
zip  
  
RUN wget -qO-
http://download.osgeo.org/gdal/${GDAL_VERSION}/gdal-${GDAL_VERSION}.tar.gz \  
| tar -xzC /usr/src \  
&& cd /usr/src/gdal-${GDAL_VERSION} \  
&& ./configure --with-python --with-spatialite \  
&& make install  
  
RUN wget -qO- https://www.open-
mpi.org/software/ompi/v${OPEN_MPI_SHORT_VERSION}/downloads/openmpi-${OPEN_MPI_VERSION}.tar.gz
\  
| tar -xzC /usr/src \  
&& cd /usr/src/openmpi-${OPEN_MPI_VERSION} \  
&& ./configure \  
&& make install \  
&& ldconfig  
  
# Download and build taudem  
# The release tags start with "v" but the folder inside the archive doesn't.  
RUN wget -qO-
https://github.com/dtarb/TauDEM/archive/v${TAUDEM_VERSION}.tar.gz \  
| tar -xzC /usr/src \  
# Remove the TestSuite directory because it contains large files  
# that we don't need.  
&& rm -rf /usr/src/TauDEM-${TAUDEM_VERSION}/TestSuite \  
&& cd /usr/src/TauDEM-${TAUDEM_VERSION}/src \  
&& make  
RUN ln -s /usr/src/TauDEM-${TAUDEM_VERSION} /opt/taudem  
ENV PATH /opt/taudem:$PATH  
  
RUN pip install --upgrade pip  

