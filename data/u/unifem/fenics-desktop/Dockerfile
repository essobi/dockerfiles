# Builds a Docker image for FEniCS (with fenicstools and sfepy) for Python3  
# based on spyder-desktop  
#  
# Authors:  
# Xiangmin Jiao <xmjiao@gmail.com>  
# Use PETSc prebuilt in compdatasci/petsc-desktop  
FROM compdatasci/spyder-desktop:latest  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
USER root  
WORKDIR /tmp  
  
# Install system packages  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
git \  
git-lfs \  
libnss3 \  
imagemagick \  
\  
libboost-filesystem-dev \  
libboost-iostreams-dev \  
libboost-math-dev \  
libboost-program-options-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libboost-timer-dev \  
libeigen3-dev \  
libomp-dev \  
libpcre3-dev \  
libhdf5-openmpi-dev \  
libgmp-dev \  
libcln-dev \  
libmpfr-dev \  
libparmetis4.0 libmetis-dev libparmetis-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
ADD image/home $DOCKER_HOME  
  
# Build FEniCS with Python3  
ENV FENICS_BUILD_TYPE=Release \  
FENICS_PREFIX=/usr/local \  
FENICS_VERSION=2017.1.0 \  
FENICS_PYTHON=python3  
  
ARG FENICS_SRC_DIR=/tmp/src  
  
# Disable testing of compilation of PETSC and SLEPC in cmake  
# cmake is broken in dolfin when using system installed PETSC and SLEPC  
ARG CMAKE_EXTRA_ARGS="-DPETSC_TEST_LIB_COMPILED=1 -DPETSC_TEST_LIB_EXITCODE=0
\  
-DSLEPC_TEST_LIB_COMPILED=1 -DSLEPC_TEST_LIB_EXITCODE=0"  
RUN $DOCKER_HOME/bin/fenics-pull && \  
$DOCKER_HOME/bin/fenics-build && \  
ldconfig && \  
rm -rf /tmp/src && \  
rm -f $DOCKER_HOME/bin/fenics-*  
  
# Install fenics-tools (this might be removed later)  
RUN cd /tmp && \  
git clone \--depth 1 https://github.com/unifem/fenicstools.git && \  
cd fenicstools && \  
python3 setup.py install && \  
rm -rf /tmp/fenicstools  
  
ENV PYTHONPATH=$FENICS_PREFIX/lib/python3/dist-packages:$PYTHONPATH  
  
# Install sfepy (without pysparse and mayavi)  
ARG SFEPY_VERSION=2017.3  
RUN pip3 install -U \  
cython \  
pyparsing \  
scikit-umfpack \  
tables \  
pymetis \  
pyamg \  
pyface && \  
pip3 install --no-cache-dir \  
https://bitbucket.org/dalcinl/igakit/get/default.tar.gz && \  
pip3 install --no-cache-dir \  
https://github.com/sfepy/sfepy/archive/release_${SFEPY_VERSION}.tar.gz  
  
########################################################  
# Customization for user  
########################################################  
USER $DOCKER_USER  
ENV GIT_EDITOR=vi EDITOR=vi  
RUN echo 'export OMP_NUM_THREADS=$(nproc)' >> $DOCKER_HOME/.profile && \  
echo "PATH=$DOCKER_HOME/bin:$PATH" >> $DOCKER_HOME/.profile  
  
WORKDIR $DOCKER_HOME  
USER root  

