FROM ubuntu:16.04  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
python \  
bash \  
git \  
vim \  
gcc \  
gfortran \  
wget \  
cmake \  
libxml2-dev \  
libpng-dev \  
make \  
cgdb \  
ssh \  
python-numpy \  
python-matplotlib \  
valgrind \  
ca-certificates \  
liblapack-dev \  
libhdf5-openmpi-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /build  
ENV PETSC_DIR=/opt/petsc-3.6.4  
# install petsc-3.6.4  
RUN wget http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.6.4.tar.gz  
RUN tar -xvzf petsc-3.6.4.tar.gz  
RUN cd petsc-3.6.4 && PETSC_DIR=$PWD python2 ./configure \  
\--prefix=/opt/petsc-3.6.4 \  
\--download-metis \  
\--download-parmetis \  
\--download-mumps \  
\--download-scalapack  
  
RUN cd petsc-3.6.4 && \  
make PETSC_DIR=/build/petsc-3.6.4 PETSC_ARCH=arch-linux2-c-debug all && \  
make PETSC_DIR=/build/petsc-3.6.4 PETSC_ARCH=arch-linux2-c-debug install  
  
# install EarthByte_Underworld  
RUN git clone https://github.com/rbeucher/EarthByte_Underworld
/opt/EarthByte_Underworld  
WORKDIR /opt/EarthByte_Underworld  
  
RUN ./configure.py --petsc-dir=$PETSC_DIR \--hdf5-dir=/usr/lib/x86_64-linux-
gnu/hdf5/openmpi/ --libxml2-lib-dir=/usr/include/libxml2/ --with-importers=0
--libxml2-lib-dir=/usr/lib/x86_64-linux-gnu/ --libxml2-inc-
dir=/usr/include/libxml2/  
RUN ./scons.py  
  
# required for earthbyte and lecode code  
ENV UW_DIR=/opt/EarthByte_Underworld/build  
RUN cd earthbyte_additions && \  
./configure.py --petsc-dir=$PETSC_DIR --libxml2-lib-dir=/usr/lib/x86_64-linux-
gnu/ --libxml2-inc-dir=/usr/include/libxml2/ && \  
./scons.py && \  
cd ..  
  
RUN cd lecode_tools && \  
./configure.py --petsc-dir=$PETSC_DIR \--libxml2-lib-
dir=/usr/lib/x86_64-linux-gnu/ --libxml2-inc-dir=/usr/include/libxml2/ && \  
./scons.py  
  
ENV PATH=$PATH:/opt/EarthByte_Underworld/build/bin  

