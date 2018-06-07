# Docker image to generate source documenation for LyX using:  
# \- Ubuntu 16.04 (Xenial)  
# \- Qt4  
# \- Autotools  
# \- Doxygen  
# \- Graphviz  
#  
# This Dockerfile is used to build a Docker image containing a set of  
# tools and libraries that can be used to build LyX's source documentation.  
#  
# The Docker image is primarily intended to be deployed on a  
# continuous integration (CI) worker, a.k.a CI node or slave. See the  
# end of this file for further details.  
#  
FROM lyxproject/build-lyx-using-ubuntu-xenial-qt4-autotools  
MAINTAINER Christian Ridderström <chr@lyx.org>  
  
# Avoid warnings during certain invocations of 'apt-get'  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add, run and then remove the script that installs packages.  
ADD ./install /install  
RUN bash /install/install_dependencies.sh && rm -rf /install  
  
# Copy scripts etc in ./build to /build in the image, e.g. to be  
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
# 4) Make the container run the script that does the actual work.  
#  
# A sequence of commands to do the above is given at the end.  
#  
# When the work is done, the script exits and the container stops,  
# leaving the results available to the CI worker in the folder  
# that was bind mounted.  
#  
# For troubleshooting the image, it's useful to start it in  
# interactive mode with a working terminal as follows:  
# docker run -i -t $IMAGE /bin/bash  
#  
# The rows below are suitable for the command section of CI job  
# (uncomment the last rows):  
# \----------------------------------------------------------------------  
#  
# With the source repository cloned to a folder $WORKSPACE, and  
# $IMAGE set to the name of the Docker image, the following will:  
# \- Start a container based on $IMAGE with $WORKSPACE bind-mounted to folder
$C_WS  
# \- Make the started container execute the script $C_SCRIPT to do the work  
# Note: Docker automatically removes the container once the script exits.  
# C_BUILD=/build # Folder in container with build scripts etc  
# C_WS=$C_BUILD/workspace # Dest. in container for bind-mounted $WORKSPACE  
# C_SCRIPT=$C_BUILD/make_doxygen_docs.sh  
# docker run --rm -v $WORKSPACE:$C_WS $IMAGE $C_SCRIPT $C_WS  

