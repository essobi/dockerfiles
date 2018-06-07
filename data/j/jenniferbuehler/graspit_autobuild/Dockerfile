# This docker image does not support graphical interfaces,  
# because support for this depends on the locally used  
# graphics card.  
# The GRASPIT environment variable is set to  
# the folder /graspit_home on the local image. So to  
# connect this folder with the GRASPIT home on your  
# computer, run with:  
#  
FROM ubuntu:14.04  
MAINTAINER Jennifer Buehler  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup environment  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
# required for saucy 13.10:  
#RUN bin/bash -c "cd /etc/apt && mkdir test && cp sources.list test/ \  
# && cd test && sed -i -- 's/archive/old-releases/g' * \  
# && cat sources.list && cp sources.list ../ && apt-get update"  
# Install system essentials  
RUN apt-get update && apt-get install -y \  
cmake \  
libsoqt4-dev \  
libcoin80-dev \  
libqt4-dev \  
libblas-dev \  
liblapack-dev \  
libqhull-dev \  
sudo \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
# need g++ for compiling with cmake even if gcc  
# is already installed  
RUN apt-get update && apt-get install -y g++ \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN bin/bash -c "mkdir -p graspit/build"  
  
COPY CMakeLists.txt /graspit/  
COPY CMakeMacros /graspit/CMakeMacros  
COPY cmdline/ /graspit/cmdline  
COPY images /graspit/images  
COPY include /graspit/include  
COPY models /graspit/models  
COPY plugins /graspit/plugins  
COPY ply /graspit/ply  
COPY qhull /graspit/qhull  
COPY src /graspit/src  
COPY test /graspit/test  
COPY tinyxml /graspit/tinyxml  
COPY ui /graspit/ui  
COPY worlds /graspit/worlds  
  
RUN bin/bash -c "cd graspit/build \  
&& cmake -DCMAKE_INSTALL_PREFIX=/usr/ .. \  
&& make \  
&& make install"  
  
RUN bin/bash -c "mkdir -p /graspit_home"  
  
ENV GRASPIT /graspit_home  
  
# setup entrypoint  
# COPY ./entrypoint /  
# ENTRYPOINT ["/entrypoint"]  
CMD ["bash"]  

