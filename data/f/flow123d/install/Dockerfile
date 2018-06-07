FROM flow123d/base  
MAINTAINER Jan Hybs  
ENV LANG C.UTF-8  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION=1.0  
  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="Flow123d" \  
org.label-schema.description="Transport Processes in Fractured Media" \  
org.label-schema.url="http://flow123d.github.io/" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/flow123d/flow123d" \  
org.label-schema.vendor="Technical University of Liberec" \  
org.label-schema.version="$VERSION" \  
org.label-schema.schema-version="1.0"  
  
RUN apt-get update && apt-get install -y \  
perl \  
python3-pip \  
python3-dev \  
libgfortran3 \  
libblas3 \  
liblapack3 \  
libhwloc5 \  
libpugixml1v5 \  
lib32z1 \  
&& sudo pip3 install \  
pyyaml \  
markdown \  
psutil \  
simplejson \  
formic \  
pymongo \  
&& rm -rf /var/lib/apt/lists/*  
  

