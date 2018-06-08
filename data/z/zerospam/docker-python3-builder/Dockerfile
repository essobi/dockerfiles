FROM python:3.6.2-alpine3.6  
  
ARG BLAS_VERSION=3.7.1  
ARG LAPACK_VERSION=3.7.1  
  
ARG NUMPY_VERSION=1.13.1  
ARG H5PY_VERSION=2.7.0  
ARG SCIPY_VERSION=0.19.1  
  
# Set one or more individual labels  
LABEL ca.zerospam.python3.builder="1.4.0"  
LABEL vendor="ZEROSPAM"  
LABEL ca.zerospam.python3.builder.release-date="2017-08-28"  
  
RUN apk --no-cache add hdf5 hdf5-dev libffi-dev --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ \  
&& apk \--update --no-cache --virtual .build-dep add \  
build-base \  
&& pip install --upgrade pip \  
&& pip install cython \  
&& pip install pytest \  
&& pip install numpy==${NUMPY_VERSION} \  
&& pip install h5py==${H5PY_VERSION} \  
&& apk del --purge hdf5-dev zlib-dev \  
&& rm -rf ~/.cache/pip/*  
  
RUN apk add --no-cache \  
ca-certificates \  
libstdc++ \  
libgfortran \  
&& apk add --virtual=build_dependencies \  
gfortran \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& mkdir -p /tmp/build \  
&& cd /tmp/build/ \  
&& wget http://www.netlib.org/blas/blas-${BLAS_VERSION}.tgz \  
&& wget http://www.netlib.org/lapack/lapack-${LAPACK_VERSION}.tgz \  
&& tar xzf blas-${BLAS_VERSION}.tgz \  
&& tar xzf lapack-${LAPACK_VERSION}.tgz \  
&& cd /tmp/build/BLAS-${BLAS_VERSION}/ \  
&& gfortran -O3 -std=legacy -m64 -fno-second-underscore -fPIC -c *.f \  
&& ar r libfblas.a *.o \  
&& ranlib libfblas.a \  
&& mv libfblas.a /tmp/build/. \  
&& cd /tmp/build/lapack-${LAPACK_VERSION}/ \  
&& sed -e "s/frecursive/fPIC/g" -e "s/ \\.\\.\// /g" -e
"s/^CBLASLIB/\\#CBLASLIB/g" make.inc.example > make.inc \  
&& make lapacklib \  
&& mv liblapack.a /tmp/build/. \  
&& cd / \  
&& export BLAS=/tmp/build/libfblas.a \  
&& export LAPACK=/tmp/build/liblapack.a \  
&& pip install scipy==${SCIPY_VERSION} \  
&& apk del --purge -r build_dependencies \  
&& rm -rf /tmp/build ~/.cache/pip/*

