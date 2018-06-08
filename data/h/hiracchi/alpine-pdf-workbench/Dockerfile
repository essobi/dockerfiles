#
------------------------------------------------------------------------------  
# buildstage  
#
------------------------------------------------------------------------------  
FROM hiracchi/alpine-buildbase as buildbase  
  
#
------------------------------------------------------------------------------  
# OpenMPI  
#
------------------------------------------------------------------------------  
FROM hiracchi/alpine-openmpi as openmpi  
  
#
------------------------------------------------------------------------------  
# ScaLAPACK  
#
------------------------------------------------------------------------------  
FROM hiracchi/alpine-scalapack as scalapack  
  
#
------------------------------------------------------------------------------  
# release stage  
#
------------------------------------------------------------------------------  
FROM hiracchi/alpine-buildbase  
MAINTAINER Toshiyuki HIRANO <hiracchi@gmail.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/hiracchi/docker-alpine-pdf" \  
org.label-schema.version=$VERSION  
  
ARG WORKDIR="/work"  
  
ENV PATH="${OPENMPI_PATH}/bin:${PATH}"
SCALAPACK_LIBRARIES="-L/opt/scalapack/lib -lscalapack -lopenblas -lgfortran"  
COPY \--from=openmpi /opt/openmpi /opt/openmpi  
COPY \--from=scalapack /opt/scalapack /opt/scalapack  
  
# python packages  
RUN set -x \  
&& pip3 install --no-cache-dir numpy  
RUN set -x \  
&& pip3 install --no-cache-dir scipy  
RUN set -x \  
&& pip3 install --no-cache-dir pandas  
RUN set -x \  
&& pip3 install --no-cache-dir matplotlib  
RUN set -x \  
&& pip3 install --no-cache-dir scikit-learn  
RUN set -x \  
&& pip3 install --no-cache-dir \  
configparser PyYAML msgpack-python beautifulsoup4  
  
# google test  
# `gtest` installed at ${WORKDIR}/gtest  
RUN set -x \  
&& cd /tmp \  
&& git clone "https://github.com/google/googletest.git" \  
&& cd googletest \  
&& mkdir -p build \  
&& cd build \  
&& cmake -DCMAKE_INSTALL_PREFIX=/opt/gtest .. \  
&& make \  
&& make install \  
&& python3 /tmp/googletest/googletest/scripts/fuse_gtest_files.py ${WORKDIR} \  
&& rm -rf /tmp/googletest  
ENV GTEST_ROOT=/opt/gtest  
  
# scripts  
COPY bin/* /usr/local/bin/  
  
# finalize  
RUN mkdir -p ${WORKDIR}  
WORKDIR ${WORKDIR}  
  
ENV HOME=${WORKDIR}  
ENV PDF_HOME=/opt/ProteinDF  
ENV PATH="${PDF_HOME}/bin:${PATH}"  
COPY docker-entrypoint.sh /  
COPY docker-pdftest.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

