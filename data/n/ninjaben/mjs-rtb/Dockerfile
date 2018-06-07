# brainardlab/mjs-rtb  
#  
# This is part of the MatlabJobSupport project.  
# https://github.com/BrainardLab/MatlabJobSupport  
#  
# It sets an environment for running MatlabJobSupport jobs, and includes  
# dependencies for RenderToolbox4 including:  
# \- Docker  
# \- Assimp  
# \- OpenExr  
# See https://github.com/RenderToolbox/RenderToolbox4  
#  
# It is based on the image brainardlab/mjs-base, and inherits the conventions
for  
# established in that image for directories inside the contianer and
directores  
# to map in from the Docker host.  
# https://github.com/BrainardLab/MatlabJobSupport/blob/master/docker/mjs-
base/Dockerfile  
#  
# Here is a sample "docker run" command:  
#  
# docker run \  
# \--rm \  
# \--net="host" \  
# -v /var/run/docker.sock:/var/run/docker.sock \  
# -v /usr/local/MATLAB/R2016a:/usr/local/MATLAB/from-host \  
# -v /var/log/matlab:/var/log/matlab \  
# brainardlab/mjs-rtb -r "tbUse('RenderToolbox4');rtbTestInstallation();exit;"  
#  
  
FROM brainardlab/mjs-docker  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
### OpenEXR and general dependencies  
RUN apt-get update && apt-get install -y \  
libboost-all-dev \  
openexr \  
cmake \  
wget \  
pkg-config  
  
### Assimp  
WORKDIR /assimp  
RUN wget https://github.com/assimp/assimp/archive/v3.3.1.tar.gz  
RUN mkdir assimp  
RUN tar -xzf v3.3.1.tar.gz  
WORKDIR /assimp/assimp-3.3.1  
RUN cmake CMakeLists.txt -G 'Unix Makefiles' && make && make install &&
ldconfig  
  
### Make sure Matlab starts with the same version of libstdc++ that Assimp
uses  
ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libstdc++.so.6  
  
### Pre-install large toolboxes so that jobs start faster  
WORKDIR /mjs/toolboxes  
RUN git clone https://github.com/Psychtoolbox-3/Psychtoolbox-3.git \  
&& chmod -R a+w /mjs/toolboxes/Psychtoolbox-3  
RUN git clone https://github.com/RenderToolbox/RenderToolbox4.git \  
&& chmod -R a+w /mjs/toolboxes/RenderToolbox4  
RUN git clone https://github.com/RenderToolbox/SphereRendererToolbox.git \  
&& chmod -R a+w /mjs/toolboxes/SphereRendererToolbox  
  
### Configure RenderToolbox4  
COPY RenderToolbox4LocalHook.m /mjs/toolboxHooks/RenderToolbox4LocalHook.m  
  
### start in known dir so that Matlab can find startup.m  
WORKDIR /mjs  
  

