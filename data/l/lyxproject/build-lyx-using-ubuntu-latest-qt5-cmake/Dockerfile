# Docker image to build LyX using:  
# - Ubuntu <version: tagged 'latest'>  
# - Qt5  
# - CMake  
#  
# This Dockerfile is used to build a Docker image containing a set of  
# tools and libraries that can be used to build LyX from source.  
#  
# The Docker image is primarily intended to be deployed on a  
# continuous integration (CI) worker, a.k.a CI node or slave. See the  
# end of this file for further details.  
#  
FROM ubuntu:latest  
MAINTAINER Christian Ridderström <chr@lyx.org>  
  
# Avoid warnings during certain invocations to apt-get install <x>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add, run and then remove the script that installs packages.  
ADD install_dependencies.sh install_dependencies.sh  
RUN bash install_dependencies.sh && rm install_dependencies.sh  
  
# Copy scripts etc in ./build to /build in the container, e.g. to be  
# used in the container to build LyX  
ADD ./build /build  
  
# Set default starting direcory and command for the container.  
# Mainly useful for interactive troubleshooting.  
WORKDIR /build  
CMD /bin/bash  
  
#  
# Usage of Docker image  
#  
# The Docker image is intended to be used on a CI worker, typically  
# through a CI job on a CI server, where the CI job would e.g.:  
#  
# 1) Clone the source repository to a folder on the CI worker  
# 2) Start a Docker container (process), using the Docker image as a  
# template.  
# 3) "Bind-mount" the folder with the LyX source to the container,  
# making the folder and LyX source available to the container.  
# 4) Make the container run the script that builds LyX  
#  
# A Docker command to do the above is given at the end.  
#  
# When the build is done, the build script will exit and the container  
# will stop. The build results are then available to the CI worker in  
# the folder that was bind mounted.  
#  
# For troubleshooting the containerr, it's useful to start it in  
# interactive mode with a working terminal as follows:  
# docker run -i -t $IMAGE /bin/bash  
#  
# The rows below are suitable for the command section of CI job  
# (uncomment the last two rows):  
# ----------------------------------------------------------------------  
#  
# With the source repository cloned to a folder $WORKSPACE, and $IMAGE  
# set to the name of this Docker image, the following commands will:  
# - Start a Docker container (process) based on this image with folder  
# $WORKSPACE bind-mounted to $SRC in the container  
# - Make the container execute the script 'build_lyx.sh' that builds LyX  
# Note: Once the build script is done, the script exits and the  
# container stops and is automatically removed.  
# SRC=/build/lyx # Dest. of bind-mounted $WORKSPACE in the container  
# docker run --rm -v $WORKSPACE:$SRC $IMAGE /build/build_lyx.sh $SRC  

