# Builds a Docker image with Ubuntu 17.10, Octave, Python3 and Jupyter
Notebook for FastSolve  
#  
# Authors:  
# Xiangmin Jiao <xmjiao@gmail.com>  
FROM compdatasci/octave-desktop:latest  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
USER root  
WORKDIR /tmp  
  
# Install system packages  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
cmake \  
zip unzip \  
bison \  
flex \  
git \  
bash-completion \  
bsdtar \  
rsync \  
wget \  
gdb \  
ccache \  
libhdf5-dev \  
libcgns-dev \  
openmpi-bin \  
liblapack-dev \  
libopenmpi-dev \  
libopenblas-dev && \  
apt-get clean && \  
pip3 install -U \  
requests \  
progressbar2 \  
PyDrive && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install PETSc from source.  
ENV PETSC_VERSION=3.7.7 \  
OPENBLAS_NUM_THREADS=1 \  
OPENBLAS_VERBOSE=0  
RUN curl -s http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-
lite-${PETSC_VERSION}.tar.gz | \  
tar zx && \  
cd petsc-${PETSC_VERSION} && \  
unset PETSC_DIR && \  
\  
mkdir -p /tmp/archive && \  
./configure --COPTFLAGS="-O2" \  
\--CXXOPTFLAGS="-O2" \  
\--FOPTFLAGS="-O2" \  
\--with-blas-lib=/usr/lib/x86_64-linux-gnu/libopenblas.so \  
\--with-lapack-lib=/usr/lib/x86_64-linux-gnu/liblapack.so \  
\--with-c-support \  
\--with-debugging=0 \  
\--with-shared-libraries \  
\--download-suitesparse \  
\--download-scalapack \  
\--download-ptscotch \  
\--download-hypre \  
\--download-mumps \  
\--download-blacs \  
\--download-spai \  
\--prefix=/usr/local/petsc-$PETSC_VERSION && \  
make all test && \  
make install && \  
rm -rf /tmp/* /var/tmp/*  
  
ENV PETSC_DIR=/usr/local/petsc-$PETSC_VERSION  
ENV LD_LIBRARY_PATH=$PETSC_DIR/lib  
  
########################################################  
# Customization for user  
########################################################  
RUN echo "export OMP_NUM_THREADS=\$(nproc)" >> $DOCKER_HOME/.profile && \  
touch $DOCKER_HOME/.log/jupyter.log && \  
chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME  
  
WORKDIR $DOCKER_HOME  

