## Container containing a MPI Application running with Torque scheduling
server  
## inside Ubuntu 16.04 and access via ssh to a 'app' user.  
## To use as a service, SSH to this container as user app.  
## It is suggested to put job scripts in /scratch (that you might  
## want to create as a data volume for efficiency  
##  
## Note! Torque-mom requires that 'ulimit -l unlimited' is set. To achieve  
## This, you need to run this container with the '--privileged' option  
  
# Based on image parana/torque which use phusion/baseimage as base image.  
  
# Note also that I use phusion because, as explained on the  
# http://phusion.github.io/baseimage-docker/ page, it automatically  
# contains and starts all needed services (like logging), it  
# takes care of sending around signals when stopped, etc.  
  
FROM parana/torque  
  
MAINTAINER João Antonio Ferreira <joao.parana@gmail.com>  
  
# Install required packages  
  
# RUN echo "deb http://cz.archive.ubuntu.com/ubuntu xenial main universe" >>
/etc/apt/sources.list  
  
RUN apt-get update \  
&& apt-get install -y \  
curl sudo mpich  
  
# && rm -rf /var/lib/apt/lists/* \  
# && apt-get clean all  
#  
  
# ### User to run job with the scheduler (root not allowed) ###  
#  
# ## Put the script for the initial setup of the authorized_keys of the app
user  
  
# # Use baseimage-docker's init system.  
# CMD ["/sbin/my_init"]  
  
VOLUME /home/app/desenv/mpi  
  
USER root  
  
  

