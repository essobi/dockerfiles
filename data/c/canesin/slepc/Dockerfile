FROM canesin/petsc:latest  
MAINTAINER Fabio C. Canesin, fabio.canesin@gmail.com  
  
# User clang as default compiler (this is redudant from canesin/petsc  
# but I repeat this here for explicity)  
ENV CC clang  
ENV CXX clang++  
ENV PETSC_DIR /opt/petsc  
  
# Compile SLEPc with latest clang  
RUN apk add \--no-cache curl build-base gfortran clang perl cmake python
linux-headers && \  
cd /tmp/ && \  
curl -L https://bitbucket.org/slepc/slepc/get/maint.tar.gz | tar xz && \  
cd `ls | grep slepc` && \  
./configure --prefix=/opt/slepc && \  
make && \  
make install && \  
apk del curl build-base gfortran clang perl cmake python linux-headers && \  
rm -rf /usr/share/man/* /tmp/* /var/cache/apk/*  
  
# Setup SLEPc location  
ENV SLEPC_DIR /opt/slepc  

