# Build the knxd Docker container  
#  
# note: debian:jessie is not the smallest possible environment - but as it  
# is expected that also an Apache with PHP is run the same environment was  
# chosen to have an overall optimization.  
# An obvious choice for a smaller enviroment could be e.g. debian:stable-slim  
  
FROM debian:jessie as builder  
  
ARG BUILD_TAG  
RUN echo BUILD_TAG: ${BUILD_TAG}  
# debug  
#ARG MY_ARG  
#ARG MY_ARG2=default4MA2  
#ARG SOURCE_BRANCH  
#ARG SOURCE_COMMIT  
#ARG COMMIT_MSG  
#ARG DOCKER_REPO  
#ARG CACHE_TAG  
#ARG IMAGE_NAME  
#RUN echo MY_ARG: ${MY_ARG}  
#RUN echo MY_ARG2: ${MY_ARG2}  
#RUN echo MY_ARG3: ${MY_ARG3:-def4ma3}  
#RUN echo SOURCE_BRANCH: ${SOURCE_BRANCH}  
#RUN echo SOURCE_COMMIT: ${SOURCE_COMMIT}  
#RUN echo COMMIT_MSG: ${COMMIT_MSG}  
#RUN echo DOCKER_REPO: ${DOCKER_REPO}  
#RUN echo CACHE_TAG: ${CACHE_TAG}  
#RUN echo IMAGE_NAME: ${IMAGE_NAME}  
# debug  
  
ENV BUILD_PACKAGES \  
autoconf \  
automake \  
autotools-dev \  
build-essential \  
cmake \  
debhelper \  
dh-systemd \  
git-core \  
libev-dev \  
libsystemd-daemon-dev \  
libsystemd-dev \  
libtool \  
libusb-1.0-0-dev \  
pkg-config  
  
RUN apt-get update && apt-get -y install $BUILD_PACKAGES  
  
# build knxd  
  
RUN git clone https://github.com/knxd/knxd.git && cd knxd && git checkout
tags/${BUILD_TAG} \  
&& dpkg-buildpackage -b -uc  
  
# install in a fresh and thus clean environment  
  
FROM debian:jessie  
  
LABEL maintainer="Christian Mayer docker@cometvisu.org" \  
description="The knxd to access the KNX bus."  
  
COPY --from=builder /knxd_*.deb /knxd-tools_*.deb ./  
RUN apt-get update && apt-get -y install libev4 libusb-1.0-0 init-system-
helpers \  
&& dpkg -i knxd_*.deb knxd-tools_*.deb  
  
# needs fix for socket exposure on volume with root<->user first  
#RUN groupadd -r knxduser && useradd --no-log-init -r -g knxduser knxduser  
#USER knxduser  
  
EXPOSE 6720  
  
CMD ["knxd"]  

