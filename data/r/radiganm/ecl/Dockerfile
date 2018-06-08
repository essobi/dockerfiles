## Dockerfile for ECL  
## Mac Radigan  
FROM ubuntu:latest  
  
MAINTAINER Mac Radigan  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
## update APT  
RUN ulimit -n 1024  
RUN apt-get update --fix-missing  
  
## install packages  
RUN apt-get update && \  
apt-get install -y \  
git \  
autoconf \  
automake \  
build-essential \  
gfortran \  
fftw3-dev \  
libncurses-dev \  
cmake \  
libgc-dev \  
libgmp3-dev \  
libatomic-ops-dev \  
libfuse-dev \  
libglew-dev \  
freeglut3-dev \  
libglm-dev  
  
RUN mkdir -p /opt  
RUN (cd /opt; git clone https://github.com/radiganm/ecl.git ./ecl)  
RUN (cd /opt/ecl; ./configure && make && make install)  
  
# clean up APT  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ECL entry point  
ADD ./ecl_ctl /usr/bin  
RUN chmod 775 /usr/bin/ecl_ctl  
ENTRYPOINT ["/usr/bin/ecl_ctl"]  
  
## *EOF*  

