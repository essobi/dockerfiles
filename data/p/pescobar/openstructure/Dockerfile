FROM centos:7.3.1611  
MAINTAINER Pablo Escobar <pablo.escobarlopez@unibas.ch>  
  
ENV OPENSTRUCTURE_VERSION=1.6.0  
ENV OPENMM_VERSION=6.1  
ENV PYTHONPATH="/usr/local/lib64/python2.7/site-packages/:${PYTHONPATH}"  
ENV
LD_LIBRARY_PATH="/usr/local/lib64/:/usr/local/openmm/lib/:${LD_LIBRARY_PATH}"  
ENV PATH="/usr/local/openmm/bin/:${PATH}"  
RUN yum makecache fast && \  
yum -y install epel-release && \  
yum -y install \  
gcc \  
gcc-c++ \  
gcc-gfortran \  
make \  
unzip \  
wget \  
tcl \  
glibc-common \  
glibc-devel \  
libjpeg-turbo \  
freetype \  
libpng \  
mesa-libGL-devel \  
mesa-libGLU-devel \  
cmake \  
python-devel \  
openblas-devel \  
openblas-static \  
eigen3-devel \  
numpy \  
boost-devel \  
PyQt4-devel \  
libtiff-devel \  
libpng-devel \  
zlib-devel \  
perl-devel \  
fftw-static \  
swig \  
doxygen \  
&& yum -y clean all  
  
# install openmm https://github.com/pandegroup/openmm  
WORKDIR /usr/local/src  
RUN wget -O openmm-${OPENMM_VERSION}.tar.gz
https://github.com/pandegroup/openmm/archive/${OPENMM_VERSION}.tar.gz && \  
tar xvf openmm-${OPENMM_VERSION}.tar.gz && \  
mkdir /usr/local/src/openmm-${OPENMM_VERSION}/build && \  
cd /usr/local/src/openmm-${OPENMM_VERSION}/build && \  
cmake .. && \  
make && \  
make install  
  
# download OpenStructure sources tarball  
WORKDIR /usr/local/src  
RUN wget -O openstructure-${OPENSTRUCTURE_VERSION}.tar.gz
"https://git.scicore.unibas.ch/schwede/openstructure/repository/archive.tar.gz?ref=${OPENSTRUCTURE_VERSION}"
&& \  
mkdir /usr/local/src/openstructure-${OPENSTRUCTURE_VERSION}-source && \  
tar -xf openstructure-${OPENSTRUCTURE_VERSION}.tar.gz --strip-components=1 -C
/usr/local/src/openstructure-${OPENSTRUCTURE_VERSION}-source && \  
mkdir /usr/local/src/openstructure-${OPENSTRUCTURE_VERSION}-source/build  
  
# compile OpenStructure  
WORKDIR /usr/local/src/openstructure-${OPENSTRUCTURE_VERSION}-source/build  
RUN cmake .. \  
-DENABLE_MM=1 \  
-DOPEN_MM_LIBRARY=/usr/local/openmm/lib/libOpenMM.so \  
-DOPEN_MM_PLUGIN_DIR=/usr/local/openmm/lib/plugins \  
-DOPEN_MM_INCLUDE_DIR=/usr/local/openmm/include \  
-DCOMPILE_TMTOOLS=1 \  
-DENABLE_GFX=ON \  
-DENABLE_GUI=ON \  
-DUSE_NUMPY=1 && \  
make && \  
make check && \  
make install  
  
RUN rm -fr /usr/local/src/openstructure-${OPENSTRUCTURE_VERSION}-source/  
  
ENTRYPOINT ["/usr/local/bin/ost"]  

