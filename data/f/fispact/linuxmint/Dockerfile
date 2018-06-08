FROM vcatechnology/linux-mint:18.0  
MAINTAINER UKAEA <admin@fispact.ukaea.uk>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="Linux Mint docker image for FISPACT-II" \  
org.label-schema.url="http://fispact.ukaea.uk/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/fispact/docker_linuxmint" \  
org.label-schema.vendor="UKAEA" \  
org.label-schema.version=$VERSION \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.schema-version="1.0"  
  
ENV RUN_SCRIPT ~/.bashrc  
  
# Install additional packages  
RUN apt-get \--yes update && \  
apt-get \--yes upgrade && \  
apt-get \--yes install gfortran g++ make cmake less python3 python3-pip
python-dev && \  
apt-get \--yes install git build-essential doxygen cloc rsync cpio
libquadmath0 && \  
pip3 install --upgrade pip && \  
pip3 install pytest pytest-xdist pypact  
  
WORKDIR /  
  
CMD /bin/bash $RUN_SCRIPT  

