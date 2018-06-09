FROM centos  
MAINTAINER d9magai  
  
ENV TREEFROGFRAMEWORK_PREFIX /opt/treefrogframework  
ENV TREEFROGFRAMEWORK_SRC_DIR ${TREEFROGFRAMEWORK_PREFIX}/src  
ENV TREEFROGFRAMEWORK_VERSION 1.12.0  
ENV TREEFROGFRAMEWORK_BASE_DIR ${TREEFROGFRAMEWORK_SRC_DIR}/treefrog-
framework-${TREEFROGFRAMEWORK_VERSION}  
ENV TREEFROGFRAMEWORK_ARCHIVE_URL
https://github.com/treefrogframework/treefrog-
framework/archive/v${TREEFROGFRAMEWORK_VERSION}.tar.gz  
  
RUN yum update -y && yum install -y \  
epel-release \  
centos-release-scl \  
&& yum clean all  
RUN yum update -y && yum install -y \  
devtoolset-3-gcc-c++ \  
make \  
gdb \  
qt5-qtbase-devel \  
qt5-qtbase-mysql \  
qt5-qtdeclarative-devel \  
which \  
&& yum clean all  
  
ENV PATH /opt/rh/devtoolset-3/root/bin/:/usr/lib64/qt5/bin:${PATH}  
RUN mkdir -p ${TREEFROGFRAMEWORK_SRC_DIR} \  
&& curl -sL ${TREEFROGFRAMEWORK_ARCHIVE_URL} | tar xz -C
${TREEFROGFRAMEWORK_SRC_DIR} \  
&& cd ${TREEFROGFRAMEWORK_BASE_DIR} \  
&& ./configure --prefix=${TREEFROGFRAMEWORK_PREFIX} \  
&& cd ${TREEFROGFRAMEWORK_BASE_DIR}/src \  
&& make -s \  
&& make -s install \  
&& cd ${TREEFROGFRAMEWORK_BASE_DIR}/tools \  
&& make -s \  
&& make -s install \  
&& rm -rf ${TREEFROGFRAMEWORK_SRC_DIR}  
  
RUN echo ${TREEFROGFRAMEWORK_PREFIX}/lib >
/etc/ld.so.conf.d/treefrogframework.conf && ldconfig  
ENV PATH ${TREEFROGFRAMEWORK_PREFIX}/bin:${PATH}  
  
EXPOSE 8800  
WORKDIR /srv/  
CMD ["tspawn", "-h"]  
  

