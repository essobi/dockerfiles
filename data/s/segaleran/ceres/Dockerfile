FROM ubuntu:16.04  
MAINTAINER Eran Segal <eran@sphericalcow.io>  
  
USER root  
ARG NUM_CORES=2  
## Install packages  
RUN apt-get update -q && \  
apt-get install -y --fix-missing --no-install-recommends \  
# Basics  
ca-certificates wget curl build-essential checkinstall unzip autoconf automake
libtool g++ yasm cmake git \  
# google-glog + gflags  
libgoogle-glog-dev \  
# BLAS & LAPACK  
libatlas-base-dev \  
# Eigen3  
libeigen3-dev \  
# SuiteSparse and CXSparse (optional)  
# - If you want to build Ceres as a *static* library (the default)  
# you can use the SuiteSparse package in the main Ubuntu package  
# repository:  
libsuitesparse-dev \  
# - However, if you want to build Ceres as a *shared* library, you must  
# add the following PPA:  
#sudo add-apt-repository ppa:bzindovic/suitesparse-bugfix-1319687  
#sudo apt-get update  
#sudo apt-get install libsuitesparse-dev  
# Sphinx (for documentation)  
python-sphinx  
  
  
WORKDIR /tmp  
RUN git clone \--depth=1 https://ceres-solver.googlesource.com/ceres-solver &&
\  
cd ceres-solver && \  
mkdir build && \  
cd build && \  
cmake -DOPENMP=OFF \  
-DCXX11=ON \  
-DBUILD_DOCUMENTATION=ON \  
.. && \  
make -j $NUM_CORES && \  
make test && \  
make install  
  
# cleanup  
# RUN ldconfig && \  
# apt-get autoclean && apt-get clean && \  
# rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
## Misc  
# ENV LC_ALL=C  
# RUN export uid=1000 gid=1000 && \  
# mkdir -p /home/user && \  
# echo "user:x:${uid}:${gid}:Developer,,,:/home/user:/bin/bash" >> /etc/passwd
&& \  
# echo "user:x:${uid}:" >> /etc/group && \  
# echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
# chown ${uid}:${gid} -R /home/user  
# RUN mv /tmp/gtsam /home/user/ && \  
# chown -R $uid:$gid /home/user/gtsam  
# ## Use something like this to connect to your xserver  
# # -e DISPLAY -v $HOME/.Xauthority:/home/user/.Xauthority --net=host  
# USER user  
# ENV HOME /home/user  
# WORKDIR /home/user  
# CMD /bin/bash

