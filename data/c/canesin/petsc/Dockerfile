FROM canesin/openblas:latest  
MAINTAINER Fabio C. Canesin, fabio.canesin@gmail.com  
  
# User clang as default compiler (this is redudant from canesin/openblas  
# but I repeat this here for explicity)  
ENV CC clang  
ENV CXX clang++  
  
# Compile PETSc with latest clang  
RUN apk add \--no-cache curl build-base gfortran clang perl cmake python
linux-headers && \  
cd /tmp/ && \  
curl -L http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-
lite-3.7.tar.gz | tar xz && \  
cd `ls | grep petsc` && \  
./configure PETSC_ARCH=dorcker-opt \  
CC=$CC \  
CXX=$CXX \  
\--prefix=/opt/petsc \  
\--known-64-bit-blas-indices=true \  
\--with-blas-lapack-lib=/opt/OpenBLAS/lib/libopenblas.a \  
\--download-mpich \  
\--download-superlu_dist \  
\--download-metis \  
\--download-parmetis \  
\--download-hypre \  
\--with-debugging=0 \  
COPTFLAGS='-O2 -march=ivybridge -mtune=ivybridge' \  
CXXOPTFLAGS='-O2 -march=ivybridge -mtune=ivybridge' \  
FOPTFLAGS='-O2 -march=ivybridge -mtune=ivybridge' && \  
make && \  
make install && \  
apk del curl build-base gfortran clang perl cmake python linux-headers && \  
rm -rf /usr/share/man/* /tmp/* /var/cache/apk/*  
  
# Setup PETSc location  
ENV PETSC_DIR /opt/petsc  

