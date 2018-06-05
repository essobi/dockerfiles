# brainardlab/mjs-brainard  
#  
# This is part of the MatlabJobSupport project.  
# https://github.com/BrainardLab/MatlabJobSupport  
#  
# It sets an environment for running MatlabJobSupport jobs, and includes  
# pre-cloned repositories for several toolboxes often used in the Brainard  
# lab. Including these here in the image will make jobs start faster.  
# \- Psychtoolbox-3  
# \- isetbio  
# \- BrainardLabToolbox  
#  
# It is based on the image brainardlab/mjs-base, and inherits the conventions
for  
# established in that image for directories inside the contianer and
directores  
# to map in from the Docker host.  
# https://github.com/BrainardLab/MatlabJobSupport/blob/master/docker/mjs-
base/Dockerfile  
#  
  
FROM brainardlab/mjs-base  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
### Pre-install large toolboxes so that jobs start faster  
WORKDIR /mjs/toolboxes  
RUN git clone https://github.com/Psychtoolbox-3/Psychtoolbox-3.git \  
&& chmod -R a+w /mjs/toolboxes/Psychtoolbox-3  
RUN git clone https://github.com/isetbio/isetbio.git \  
&& chmod -R a+w /mjs/toolboxes/isetbio  
RUN git clone https://github.com/BrainardLab/BrainardLabToolbox.git \  
&& chmod -R a+w /mjs/toolboxes/BrainardLabToolbox  
  
### start in known dir so that Matlab can find startup.m  
WORKDIR /mjs  

