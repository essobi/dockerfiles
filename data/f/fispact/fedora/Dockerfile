FROM fedora:26  
MAINTAINER UKAEA <admin@fispact.ukaea.uk>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="Fedora docker image for FISPACT-II" \  
org.label-schema.url="http://fispact.ukaea.uk/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/fispact/docker_fedora" \  
org.label-schema.vendor="UKAEA" \  
org.label-schema.version=$VERSION \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.schema-version="1.0"  
  
# some environment variables for regression testing  
ENV FISPACT_SYSTEM_TESTS_REF fedora_26_gfortran_7_xsbinaries  
ENV PYTHONDONTWRITEBYTECODE 1.  
ENV PYTEST_VERBOSE line  
  
ENV RUN_SCRIPT ~/.bashrc  
  
WORKDIR /  
  
# Install additional packages  
RUN yum install -y wget which make less doxygen rsync nano && \  
yum install -y cpio libgcc gcc gcc-c++ gcc-gfortran && \  
yum install -y libgfortran-static libstdc++-static && \  
yum install -y libstdc++.i686 libgcc.i686 && \  
yum install -y cmake python3 python3-devel git && \  
pip3 install --upgrade pip && \  
pip3 install pytest pytest-xdist pypact  
  
CMD /bin/bash $RUN_SCRIPT  

