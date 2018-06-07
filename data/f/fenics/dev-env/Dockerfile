# Builds a Docker image with the necessary libraries for compiling  
# FEniCS with Python 3. The image is at:  
#  
# https://hub.docker.com/r/fenics/dev-env  
#  
# Authors:  
# Jack S. Hale <jack.hale@uni.lu>  
# Lizao Li <lzlarryli@gmail.com>  
# Garth N. Wells <gnw20@cam.ac.uk>  
# Jan Blechta <blechta@karlin.mff.cuni.cz>  
  
FROM fenics/base:py3  
LABEL maintainer "Xiangmin Jiao <xiangmin.jiao@stonybrook.edu>"  
  
USER root  
WORKDIR /tmp  
  
# Environment variables  
ENV PETSC_VERSION=3.7.5 \  
SLEPC_VERSION=3.7.3 \  
SWIG_VERSION=3.0.12 \  
MPI4PY_VERSION=2.0.0 \  
PETSC4PY_VERSION=3.7.0 \  
SLEPC4PY_VERSION=3.7.0 \  
TRILINOS_VERSION=12.10.1 \  
OPENBLAS_NUM_THREADS=1 \  
OPENBLAS_VERBOSE=0 \  
GIT_LFS_VERSION=2.0.1  
  
# We also need to get a newer version of cmake  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | sudo bash && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
git-lfs=${GIT_LFS_VERSION} && \  
apt-get install -y --no-install-recommends \  
bison \  
doxygen \  
flex \  
\  
build-essential \  
g++ \  
gfortran \  
pkg-config \  
ccache \  
cmake \  
\  
libbz2-dev \  
libssl-dev \  
libreadline-dev \  
libsqlite3-dev \  
tk-dev \  
libpng-dev \  
libfreetype6-dev \  
\  
python \  
python3-pip \  
python3-dev \  
python3-flufl.lock \  
python3-numpy \  
python3-ply \  
python3-pytest \  
python3-scipy \  
python3-six \  
python3-urllib3 \  
\  
libboost-filesystem-dev \  
libboost-iostreams-dev \  
libboost-program-options-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libboost-timer-dev \  
libeigen3-dev \  
liblapack-dev \  
libmpich-dev \  
libopenblas-dev \  
libpcre3-dev \  
libhdf5-mpich-dev \  
libgmp-dev \  
libcln-dev \  
libmpfr-dev \  
mpich && \  
git lfs install && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install PETSc from source.  
RUN curl -s http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-
lite-${PETSC_VERSION}.tar.gz | \  
tar zx && \  
cd petsc-${PETSC_VERSION} && \  
./configure --COPTFLAGS="-O2" \  
\--CXXOPTFLAGS="-O2" \  
\--FOPTFLAGS="-O2" \  
\--with-blas-lib=/usr/lib/libopenblas.a --with-lapack-lib=/usr/lib/liblapack.a
\  
\--with-c-support \  
\--with-debugging=0 \  
\--with-shared-libraries \  
\--download-suitesparse \  
\--download-superlu \  
\--download-superlu_dist \  
\--download-scalapack \  
\--download-metis \  
\--download-parmetis \  
\--download-ptscotch \  
\--download-hypre \  
\--download-mumps \  
\--download-blacs \  
\--download-spai \  
\--download-ml \  
\--prefix=/usr/local/petsc-32 && \  
make && \  
make install && \  
rm -rf /tmp/*  
  
# Install SLEPc from source  
RUN mkdir slepc-src && \  
curl -s https://bitbucket.org/slepc/slepc/get/v${SLEPC_VERSION}.tar.gz | \  
tar zx -C slepc-src --strip-components 1 && \  
export PETSC_DIR=/usr/local/petsc-32 && \  
cd slepc-src && \  
./configure --prefix=/usr/local/slepc-32 && \  
make && \  
make install && \  
rm -rf /tmp/*  
  
# By default use the 32-bit build of SLEPc and PETSc.  
ENV SLEPC_DIR=/usr/local/slepc-32 \  
PETSC_DIR=/usr/local/petsc-32  
  
# Helper scripts  
ADD image $DOCKER_HOME  
  
# Install sympy, mpi4py, petsc4py and slepc4py and Swig from source.  
RUN pip3 install -U pip setuptools && \  
pip3 install -U ipython sympy matplotlib && \  
pip3 install
https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-${MPI4PY_VERSION}.tar.gz
&& \  
pip3 install
https://bitbucket.org/petsc/petsc4py/downloads/petsc4py-${PETSC4PY_VERSION}.tar.gz
&& \  
pip3 install
https://bitbucket.org/slepc/slepc4py/downloads/slepc4py-${SLEPC4PY_VERSION}.tar.gz
&& \  
curl -s -L http://downloads.sourceforge.net/swig/swig-${SWIG_VERSION}.tar.gz |
tar zx && \  
cd swig-${SWIG_VERSION} && \  
./configure && \  
make && \  
make install && \  
rm -rf /tmp/* && \  
echo "alias python=python3" >> $DOCKER_HOME/.bashrc && \  
chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME  
  
WORKDIR $DOCKER_HOME  

