FROM jameshclrk/parmetis:latest  
  
MAINTAINER James Clark <james.clark@stfc.ac.uk>  
  
ARG PETSC_VERSION=3.7.6  
ARG PETSC_INSTALL_PATH=/opt/petsc  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y bison flex  
  
RUN set -x \  
&& curl -fSL "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-
lite-${PETSC_VERSION}.tar.gz" -o petsc.tar.gz \  
&& mkdir -p /usr/src/petsc \  
&& tar -xf petsc.tar.gz -C /usr/src/petsc \--strip-components=1 \  
&& rm petsc.tar.gz* \  
&& cd /usr/src/petsc \  
&& ./configure \  
\--with-debugging=0 \  
\--with-shared-libraries=1 \  
\--with-metis \  
\--with-metis-include="${PARMETIS_DIR}/include" \  
\--with-metis-lib=[-L${PARMETIS_DIR}/lib,-lmetis] \  
\--with-parmetis \  
\--with-parmetis-include="${PARMETIS_DIR}/include" \  
\--with-parmetis-lib=[-L${PARMETIS_DIR}/lib,-lparmetis] \  
\--download-triangle \  
\--download-ctetgen \  
\--download-chaco \  
\--download-exodusii \  
\--download-netcdf \  
\--download-hdf5 \  
\--download-ptscotch \  
\--download-fblaslapack \  
\--prefix=${PETSC_INSTALL_PATH} \  
PETSC_ARCH=linux-gnu-c-shared \  
&& make all \  
&& make test \  
&& make install \  
&& make PETSC_DIR="${PETSC_INSTALL_PATH}" PETSC_ARCH="" test \  
&& rm -rf /usr/src/petsc  
  
ENV PATH="${PETSC_INSTALL_PATH}/bin:${PATH}"
LD_LIBRARY_PATH="${PETSC_INSTALL_PATH}/lib:${LD_LIBRARY_PATH}"
PETSC_DIR="${PETSC_INSTALL_PATH}"  

