# brainardlab/mjs-docker  
#  
# This is part of the MatlabJobSupport project.  
# https://github.com/BrainardLab/MatlabJobSupport  
#  
# It sets an environment for running MatlabJobSupport jobs, which includes a  
# Docker client. This client can be connected to the Docker daemon running  
# on the host.  
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
# brainardlab/mjs-docker -r "system('docker run hello-world');exit;"  
#  
  
FROM brainardlab/mjs-base  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
### Docker client inside the container  
RUN apt-get update && apt-get install -y docker.io  
  

