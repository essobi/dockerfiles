# DOCKER-VERSION 1.0  
FROM dit4c/dit4c-container-ipython  
MAINTAINER t.dettrick@uq.edu.au  
  
ENV PETSC_VERSION 3.5.3  
RUN yum install -y \  
mercurial \  
libxml2-devel libpng-devel \  
openmpi-devel hdf5-openmpi-static \  
hostname time \  
gdal-devel geos-devel proj-devel libxml2-devel libxslt-devel \  
mesa-libOSMesa-devel mesa-libGLU-devel libX11-devel  
  
# Add extra geo-related python packages for teaching  
RUN su researcher -c "CPLUS_INCLUDE_PATH=/usr/include/gdal
C_INCLUDE_PATH=/usr/include/gdal \  
/opt/python/bin/pip install PIL shapely fiona geopandas basemap cartopy
rasterio obspy gdal"  
  
RUN yum install -y udunits2 grib_api && \  
su researcher -c "/opt/python/bin/pip install biggus pyke cdat-lite==6.0rc2"
&& \  
su researcher -c "/opt/python/bin/pip install
https://github.com/SciTools/iris/archive/v1.7.4.tar.gz"  
  
# Install PETSc  
RUN cd /tmp && \  
wget -nv "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-
lite-$PETSC_VERSION.tar.gz" && \  
tar xzf petsc-lite-$PETSC_VERSION.tar.gz && \  
cd petsc-$PETSC_VERSION && \  
export LD_LIBRARY_PATH=/usr/lib64/openmpi/lib:$LD_LIBRARY_PATH && \  
./configure --prefix=/usr/local/petsc --download-fblaslapack --with-mpi-
dir=/usr/lib64/openmpi --with-pic=1 && \  
make all test && \  
make install && \  
cd /tmp && \  
rm -r petsc-$PETSC_VERSION  
  
RUN hg clone -b newInterface
https://bitbucket.org/underworldproject/underworld2 /opt/underworld  
  
COPY /etc /etc  
  
## Disabled until a more modern version of ffmpeg is supported by Underworld  
#RUN rpm --import /etc/RPM-GPG-KEY.atrpms && \  
# rpm -Uvh http://dl.atrpms.net/all/atrpms-repo-7-7.el7.x86_64.rpm && \  
# yum install -y ffmpeg-devel  
# Compile Underworld & gLucifer  
# Note: CFLAGS isn't required - it just squelches the enormous number of
compile  
# warnings which would otherwise clutter the build log.  
RUN cd /opt/underworld/libUnderworld && \  
./configure.py --help && \  
export PATH=$PATH:/usr/lib64/openmpi/bin && \  
export PETSC_ARCH=linux-gnu && \  
export PETSC_DIR=/usr/local/petsc && \  
export LD_LIBRARY_PATH=/usr/lib64/openmpi/lib:$LD_LIBRARY_PATH && \  
source /opt/python/bin/activate && \  
./configure.py --cxx=/usr/lib64/openmpi/bin/mpicxx
--cc=/usr/lib64/openmpi/bin/mpicc --mpi-lib-dir=/usr/lib64/openmpi/lib --mpi-
inc-dir=/usr/include/openmpi-x86_64 && \  
./scons.py && \  
(rm /opt/underworld/libUnderworld/build/bin/LavaVu || true)  

