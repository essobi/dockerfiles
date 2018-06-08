FROM opensuse:42.3  
MAINTAINER UKAEA <admin@fispact.ukaea.uk>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="openSUSE docker image for FISPACT-II" \  
org.label-schema.url="http://fispact.ukaea.uk/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/fispact/docker_opensuse" \  
org.label-schema.vendor="UKAEA" \  
org.label-schema.version=$VERSION \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.schema-version="1.0"  
  
# some environment variables for regression testing  
ENV FISPACT_SYSTEM_TESTS_REF opensuse_42.3_gfortran_7_xsbinaries  
ENV PYTHONDONTWRITEBYTECODE 1.  
ENV PYTEST_VERBOSE line  
  
ENV RUN_SCRIPT ~/.bashrc  
  
# Install additional packages  
RUN zypper in -y python3 python3-devel python3-pip && \  
zypper in -y gcc7 gcc7-fortran gcc7-c++ && \  
zypper in -y make cmake less sudo doxygen rsync which nano git && \  
zypper in -y libquadmath0 && \  
# symbolic link to gcc-7  
ln -s /usr/bin/gcc-7 /usr/bin/gcc && \  
ln -s /usr/bin/g++-7 /usr/bin/g++ && \  
ln -s /usr/bin/gfortran-7 /usr/bin/gfortran && \  
# pip3 packages  
pip3 install --upgrade pip && \  
pip3 install pytest pytest-xdist pypact numpy  
  
WORKDIR /  
  
CMD /bin/bash $RUN_SCRIPT  

