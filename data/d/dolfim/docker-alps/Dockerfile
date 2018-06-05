FROM ubuntu:trusty  
  
MAINTAINER Michele Dolfi <dolfim@phys.ethz.ch>  
  
RUN apt-get update  
  
## Install tools  
RUN apt-get -yq install wget  
  
## Install ALPS dependencies  
RUN apt-get -yq install build-essential gfortran cmake \  
libhdf5-serial-dev libfftw3-dev gfortran python-matplotlib \  
python-scipy liblapack-dev xsltproc python-dev libboost-all-dev  
  
## Download sources  
RUN mkdir src && cd src; \  
wget http://alps.comp-
phys.org/static/software/releases/alps-2.2.b4-src.tar.gz; \  
tar xzf alps-2.2.b4-src.tar.gz  
  
## Compile and install ALPS  
RUN cd src/alps-2.2.b4-src; \  
mkdir build && cd build; \  
cmake -DALPS_BUILD_FORTRAN=ON \  
-DALPS_ENABLE_OPENMP=ON \  
../alps; \  
make -j2; \  
ctest -j2; \  
make install -j2  
  
## remove compilation folder  
RUN rm -rf src  
  
## Setup environment  
ENV PATH /opt/alps/bin:$PATH  
ENV LD_LIBRARY_PATH /opt/alps/lib:$LD_LIBRARY_PATH  
ENV PYTHONPATH /opt/alps/lib:$PYTHONPATH  
  
## Setup volumes  
RUN mkdir /output  
VOLUME /output  
WORKDIR /output  
  

