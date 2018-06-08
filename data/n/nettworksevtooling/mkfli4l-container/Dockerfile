FROM debian:stretch  
MAINTAINER Florian Wolters <fli4l@florian-wolters.de>  
  
# Define build arguments  
ARG DEVELOP_USER=developer  
ARG DEVELOP_PASS=developer  
ARG UID="1011"  
ARG GID="1011"  
# Define environment vars  
ENV WORK_DIR=/data/work \  
SHARED_DIR=/data/shared/fli4l \  
DEBIAN_FRONTEND=noninteractive \  
LC_ALL=en_US.UTF-8 \  
TZ='Europe/Berlin'  
# Mount point for development workspace  
RUN mkdir -p ${WORK_DIR}  
VOLUME ${WORK_DIR}  
# Mount point for shared resources like source archives etc  
RUN mkdir -p ${SHARED_DIR}  
VOLUME ${SHARED_DIR}  
# Setup develop account  
# Create working directory  
# Change user UID and GID  
RUN groupadd --gid ${GID} ${DEVELOP_USER} \  
&& useradd --create-home --home-dir /home/${DEVELOP_USER} \--shell /bin/bash
--uid ${UID} \--gid ${GID} ${DEVELOP_USER} \  
&& echo "${DEVELOP_USER}:${DEVELOP_USER}" | chpasswd \  
&& chown ${DEVELOP_USER}:${DEVELOP_USER} /home/${DEVELOP_USER} -R \  
&& ulimit -v unlimited  
  
RUN apt-get update -y \  
&& apt-get upgrade -y  
  
RUN apt-get install -y --no-install-recommends \  
locales \  
git \  
subversion \  
make \  
binutils \  
build-essential \  
flex \  
bison \  
file \  
doxygen \  
valgrind \  
graphviz \  
python  
  
# Set locale to UTF8  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
# Set timezone to Europe/Berlin  
RUN echo $TZ > /etc/timezone && \  
rm /etc/localtime && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata  
  

