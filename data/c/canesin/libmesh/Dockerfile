FROM canesin/slepc:latest  
MAINTAINER Fabio C. Canesin, fabio.canesin@gmail.com  
  
# User clang as default compiler (this is redudant from canesin/slepc  
# but I repeat this here for explicity)  
ENV CC clang  
ENV CXX clang++  
ENV PETSC_DIR /opt/petsc  
ENV SLEPC_DIR /opt/slepc  
ENV CPATH /opt/OpenBLAS/include:/opt/petsc/include:/opt/slepc/include  
# Compile LibMesh with latest clang  
RUN apk add \--no-cache curl build-base clang cmake && \  
cd /tmp/ && \  
curl -L https://github.com/jwpeterson/libmesh/archive/petsc_blas_int.tar.gz |
tar xz && \  
cd `ls | grep libmesh` && \  
./configure \--prefix=/opt/libmesh \  
\--with-methods="opt" \  
\--with-metis=PETSc \  
\--enable-ifem \  
\--enable-cxx11 \  
\--enable-silent-rules \  
\--enable-unique-ptr \  
\--enable-unique-id \  
\--disable-warnings \  
\--disable-timestamps \  
\--disable-fortran \  
\--disable-pthreads \  
\--disable-openmp \  
\--disable-maintainer-mode && \  
make  
RUN make install && \  
make installcheck METHODS=opt && \  
apk del curl build-base clang cmake && \  
rm -rf /usr/share/man/* /tmp/* /var/cache/apk/*  
  
# Setup LibMesh location  
ENV LIBMESH_DIR /opt/libmesh  

