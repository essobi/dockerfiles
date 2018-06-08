# vim:set ft=dockerfile:  
FROM alpine:3.7  
  
# Metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
  
ARG OPENBLAS_VERSION=0.3.0.dev  
ARG OPENBLAS_COMMIT=f5959f2543399b764ee9bf6bf1874dfb7caa9fee  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="OpenBLAS" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/slothai/docker-openblas" \  
org.label-schema.vendor="SlothAI <https://slothai.github.io/>" \  
org.label-schema.docker.cmd.debug="docker exec -it slothai/openblas /bin/sh" \  
org.label-schema.schema-version="1.0"  
  
ENV OPENBLAS_VERSION=${OPENBLAS_VERSION}  
RUN apk add \--no-cache --virtual .meta-build-dependencies \  
gfortran \  
libc-dev \  
linux-headers \  
make \  
perl && \  
wget -O openblas.tar.gz
"https://github.com/xianyi/OpenBLAS/archive/$OPENBLAS_COMMIT.tar.gz" && tar
xzf openblas.tar.gz && rm -f openblas.tar.gz && \  
cd OpenBLAS-$OPENBLAS_COMMIT && make FC=gfortran NO_AFFINITY=1 USE_OPENMP=1
OMP_NUM_THREADS=$(nproc) && make PREFIX=/opt/OpenBLAS install && \  
apk del .meta-build-dependencies && \  
rm -rf /OpenBLAS-$OPENBLAS_COMMIT  

