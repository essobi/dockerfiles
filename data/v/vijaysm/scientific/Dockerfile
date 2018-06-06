# Builds a Docker image with all the necessary compiler and  
# build essentials needed to test SIGMA packages and  
# computational toolchains.  
#  
# Authors:  
# Vijay Mahadevan <vijay.m@gmail.com>  
FROM phusion/baseimage:0.10.0  
MAINTAINER Vijay Mahadevan <vijay.m@gmail.com>  
  
ENV HOME /home/sigma  
  
# Install add-apt-repository  
# Set up user so that we do not run as root  
# See https://github.com/phusion/baseimage-docker/issues/186  
RUN apt-get -qq update \  
&& apt-get -qqy install python-software-properties \  
wget pkg-config git libopenblas-dev liblapack-dev \  
make cmake autoconf automake libtool python \  
clang gcc g++ gfortran \  
libhdf5-dev libhdf5-mpich-dev libnetcdf-c++4 \  
libeigen3-dev libmetis-dev doxygen \  
liboce-foundation-dev liboce-modeling-dev liboce-ocaf-dev liboce-
visualization-dev oce-draw \  
netgen libnglib-dev \  
python-setuptools python-numpy cython python-nose \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#RUN groupadd -r sigmauser -g 433 && useradd -u 431 -r -g sigmauser -d
/home/sigma -s /usr/sbin/nologin -c "Docker image - SIGMA user" sigmauser \  
# && chown -R sigmauser:sigmauser /home/sigma && echo "sigmauser:docker" |
chpasswd \  
# && usermod -a -G sudo sigmauser  
RUN mkdir -p /home/sigma/bin \  
&& sed -i 's/DRAWEXE//g' /usr/lib/x86_64-linux-gnu/oce-0.17/OCEConfig.cmake  
  
# This makes sure we launch with ENTRYPOINT /bin/bash into the home directory  
ADD WELCOMEMSG /home/sigma/.WELCOMEMSG  
ADD .bashrc_SIGMA /home/sigma/.bashrc  
ADD bootstrapSIGMA /home/sigma/bin/bootstrapSIGMA  
  
#ENTRYPOINT ["/sbin/setuser","sigmauser","/bin/bash","-c"]  
CMD ["/sbin/my_init"]  
  

