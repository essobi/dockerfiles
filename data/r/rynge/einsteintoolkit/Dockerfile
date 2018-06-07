# einsteintoolkit  
FROM ubuntu:16.04  
MAINTAINER Mats Rynge <rynge@isi.edu>  
  
# Install necessary Ubuntu packages  
RUN apt-get update && \  
apt-get install -y \  
curl git perl python subversion wget \  
build-essential g++ gcc gfortran make pkg-config \  
gsl-bin libgsl0-dev \  
h5utils hdf5-helpers hdf5-tools libhdf5-openmpi-dev \  
hwloc-nox libhwloc-dev libnuma-dev \  
libfftw3-bin libfftw3-dev libfftw3-mpi-dev \  
libjpeg-dev \  
libltdl-dev \  
libopenblas-dev \  
libopenmpi-dev openmpi-bin \  
libpapi-dev papi-tools \  
libssl-dev \  
petsc-dev \  
zlib1g zlib1g-dev  
  
# Download installer (need to do this as root)  
ADD https://raw.github.com/gridaphobe/CRL/ET_2016_05/GetComponents /tmp/  
ADD
https://bitbucket.org/einsteintoolkit/manifest/raw/ET_2016_05/einsteintoolkit.th
/tmp/  
RUN chmod a+rx /tmp/GetComponents && \  
chmod a+r /tmp/einsteintoolkit.th  
  
# Configure the machine  
RUN git config --global user.email "scientist@localhost" && \  
git config --global user.name "Scientist, Einstein Toolkit" && \  
echo 'einsteintoolkit' >"$HOME/.hostname"  
  
# Download the Einstein Toolkit  
WORKDIR /opt  
RUN mkdir /opt/Cactus && \  
/tmp/GetComponents --parallel /tmp/einsteintoolkit.th  
WORKDIR /opt/Cactus  
# TODO: Move these into the Einstein Toolkit  
COPY /einsteintoolkit.ini simfactory/mdb/machines/  
COPY /einsteintoolkit.cfg simfactory/mdb/optionlists/  
COPY /einsteintoolkit.sub simfactory/mdb/submitscripts/  
COPY /einsteintoolkit.run simfactory/mdb/runscripts/  
# Configure Simfactory  
COPY /defs.local.ini simfactory/etc/  
  
# Build  
RUN ./simfactory/bin/sim build  
  

