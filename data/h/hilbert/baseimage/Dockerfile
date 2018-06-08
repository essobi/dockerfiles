FROM ubuntu:14.04  
MAINTAINER Oleksandr Motsak <malex984+hilbert.baseimage@gmail.com>  
  
COPY . /bd_build  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& /bd_build/prepare.sh \  
&& /bd_build/system_services.sh \  
&& /bd_build/utilities.sh \  
&& /bd_build/cleanup.sh  
  
ENV DEBIAN_FRONTEND="teletype" \  
LANG="en_US.UTF-8" \  
LANGUAGE="en_US:en" \  
LC_ALL="en_US.UTF-8"  
  
CMD ["/sbin/my_init"]  
  
ARG IMAGE_VERSION=latest  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE=someday  
ARG VCS_REF=HEAD  
ARG VCS_URL="https://github.com/hilbert/baseimage"  
# ARG VERSION=${IMAGE_VERSION}  
ARG GIT_NOT_CLEAN_CHECK  
ARG DOCKERFILE="Dockerfile"  
  
LABEL org.label-schema.build-date="${BUILD_DATE}" \  
org.label-schema.name="Hilbert" \  
org.label-schema.description="Phusion's baseimage reverted to Ubuntu 14.04
wihtout SSHD" \  
org.label-schema.vendor="IMAGINARY gGmbH" \  
org.label-schema.url="https://hilbert.github.io" \  
org.label-schema.vcs-ref="${VCS_REF}" \  
org.label-schema.vcs-url="${VCS_URL}" \  
org.label-schema.version="${IMAGE_VERSION}" \  
org.label-schema.schema-version="1.0" \  
com.microscaling.license="Apache-2.0" \  
com.microscaling.docker.dockerfile="/image/Dockerfile" \  
IMAGE_VERSION="${IMAGE_VERSION}" \  
GIT_NOT_CLEAN_CHECK="${GIT_NOT_CLEAN_CHECK}" \  
DOCKERFILE="${DOCKERFILE}"  
  
ONBUILD LABEL org.label-schema.build-date="" \  
org.label-schema.name="" \  
org.label-schema.description="" \  
org.label-schema.vendor="" \  
org.label-schema.url="" \  
org.label-schema.vcs-ref="" \  
org.label-schema.vcs-url="" \  
org.label-schema.version="" \  
org.label-schema.schema-version="" \  
com.microscaling.license="" \  
com.microscaling.docker.dockerfile="" \  
IMAGE_VERSION="" \  
GIT_NOT_CLEAN_CHECK=""  

