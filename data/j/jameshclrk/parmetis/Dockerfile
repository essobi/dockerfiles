FROM jameshclrk/mpich:latest  
  
MAINTAINER James Clark <james.clark@stfc.ac.uk>  
  
ARG METIS_VERSION=5.1.0  
ARG PARMETIS_VERSION=4.0.3  
ARG PARMETIS_INSTALL_DIR="/opt/parmetis"  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y cmake  
  
RUN set -x \  
&& curl -fSL
"http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-$METIS_VERSION.tar.gz"
-o metis.tar.gz \  
&& mkdir -p /usr/src/metis \  
&& tar -xf metis.tar.gz -C /usr/src/metis \--strip-components=1 \  
&& rm metis.tar.gz* \  
&& cd /usr/src/metis \  
&& make config prefix="${PARMETIS_INSTALL_DIR}" \  
&& make -j"$(nproc)" \  
&& make install \  
&& rm -rf /usr/src/metis  
  
RUN set -x \  
&& curl -fSL
"http://glaros.dtc.umn.edu/gkhome/fetch/sw/parmetis/parmetis-$PARMETIS_VERSION.tar.gz"
-o parmetis.tar.gz \  
&& mkdir -p /usr/src/parmetis \  
&& tar -xf parmetis.tar.gz -C /usr/src/parmetis \--strip-components=1 \  
&& rm parmetis.tar.gz* \  
&& cd /usr/src/parmetis \  
&& dir="$(mktemp -d)" \  
&& make config prefix="${PARMETIS_INSTALL_DIR}" \  
&& make -j"$(nproc)" \  
&& make install \  
&& rm -rf /usr/src/parmetis  
  
ENV LD_LIBRARY_PATH="${PARMETIS_INSTALL_DIR}/lib:${LD_LIBRARY_PATH}"
PATH="${PARMETIS_INSTALL_DIR}/bin:$PATH"  
ENV PARMETIS_DIR="${PARMETIS_INSTALL_DIR}"  

