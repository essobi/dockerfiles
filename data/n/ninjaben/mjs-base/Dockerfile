# brainardlab/mjs-base  
#  
# This is the base image for the MatlabJobSupport project.  
# https://github.com/BrainardLab/MatlabJobSupport  
#  
# It sets up the minimum necessary environment for running MatlabJobSupport
jobs.  
#  
# It establishes conventions for directories inside the contianer  
# and directores to map in from the Docker host.  
#  
# Directories inside the container:  
# \- /mjs -- startup.m, initial dir for container startup  
# \- /mjs/ToolboxToolbox -- the ToolboxToolbox  
# \- /mjs/projects -- projects that can be deployed with ToolboxToolbox  
# \- /mjs/toolboxes -- toolboxes installed by the ToolboxToolbox  
# \- /mjs/toolboxes/ToolboxRegistry -- registry of toolboxes known to
ToolboxToolbox  
# \- /mjs/toolboxes/MatlabJobSupport -- MatlabJobSupport itself  
# \- /mjs/toolboxHooks -- local toolbox hooks created by the ToolboxToolbox  
#  
# Container directores that should map to directories on the Docker host:  
# \- /usr/local/MATLAB/from-host -- a real matlab installation (eg
/usr/local/MATLAB/R2016a)  
# \- /var/log/matlab -- where to write matlab logs  
# \- /opt/toolboxes -- where ToolboxToolbox can look for shared/pre-installed
toolboxes  
# \- INPUT_DIR -- custom dir to map from host and add to Matlab path  
# \- OUTPUT_DIR -- custom dir to map from host  
#  
# It establishes conventions for how to run job containers. For example:  
# \- use "host" networking to satisfy the Matlab license  
# \- set environmant variables to tell startup.m where to find INPUT_DIR  
# and OUTPUT_DIR.  
# \- set a WORKING_DIR environment to tell startup.m where to cd()  
#  
# Here is a sample "docker run" command:  
#  
# docker run \  
# \--rm \  
# \--net="host" \  
# -v /usr/local/MATLAB/R2016a:/usr/local/MATLAB/from-host \  
# -v /var/log/matlab:/var/log/matlab \  
# -v /home/ben/Documents/MATLAB/shared-toolboxes:/opt/toolboxes \  
# -e "INPUT_DIR=/home/ben/Documents/MATLAB/input" \  
# -v /home/ben/Documents/MATLAB/input:/home/ben/Documents/MATLAB/input \  
# -e "OUTPUT_DIR=/home/ben/Documents/MATLAB/output" \  
# -v /home/ben/Documents/MATLAB/output:/home/ben/Documents/MATLAB/outout \  
# -e "WORKING_DIR=/home/ben/Documents/MATLAB/output" \  
# brainardlab/mjs-base  
#  
  
FROM ubuntu:14.04  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
  
### Minimum environment including Matlab dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
gfortran \  
git \  
libpng12-dev \  
libfreetype6-dev \  
libblas-dev \  
liblapack-dev \  
subversion \  
xorg  
  
  
### ToolboxToolbox  
WORKDIR /mjs  
RUN git clone https://github.com/ToolboxHub/ToolboxToolbox.git  
  
WORKDIR /mjs/toolboxes  
RUN git clone https://github.com/ToolboxHub/ToolboxRegistry.git  
RUN git clone https://github.com/BrainardLab/MatlabJobSupport.git  
  
  
### Matlab startup.m and the dirs that it expects to exist  
COPY mjs-startup.m /mjs/startup.m  
RUN mkdir -p /usr/local/MATLAB/from-host  
RUN mkdir -p /var/log/matlab  
RUN mkdir -p /opt/toolboxes  
RUN mkdir -p /var/mjs  
RUN mkdir -p /mjs/projects  
  
  
### Start with fresh Matlab preferences  
RUN mkdir -p /var/mjs/matlab_prefdir  
ENV MATLAB_PREFDIR=/var/mjs/matlab_prefdir  
  
  
### Start with fresh Matlab Path  
COPY mjs-pathdef.m /mjs/pathdef.m  
  
  
### start in known dir so that Matlab can find startup.m  
WORKDIR /mjs  
ENV PATH="/usr/local/MATLAB/from-host/bin:${PATH}"  
ENTRYPOINT ["matlab", "-logfile /var/log/matlab/matlab.log"]  
CMD ["-h"]  
  

