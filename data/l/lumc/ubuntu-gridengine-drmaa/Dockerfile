# This Dockerfile is based on the docker_ubuntu_drmaa_conda Dockerfile written
by  
# John Kirkham <https://github.com/jakirkham/docker_ubuntu_drmaa_conda>.  
#  
# The following changes were made in this fork:  
# - Upgraded the base image to ubuntu:16.04 (debian:jessie-backports had
problems with something in /proc/mount)  
# - Updated the hostname change in /etc/hosts in gridengine/install_ge.sh  
# - Updated the libdrmaa package name  
# - Removed the conda installation directives and commands  
FROM ubuntu:16.04  
MAINTAINER Wibowo Arindrarto <bow@bow.web.id>  
  
RUN apt-get update -y && \  
apt-get clean  
  
ADD gridengine /usr/share/gridengine  
RUN /usr/share/gridengine/install_ge.sh  
  
ENV SGE_CONFIG_DIR=/usr/share/gridengine \  
SGE_ROOT=/var/lib/gridengine \  
SGE_CELL=default \  
DRMAA_LIBRARY_PATH=/usr/lib/gridengine-drmaa/lib/libdrmaa.so.1.0  
ADD docker /usr/share/docker  
RUN /usr/share/docker/install_tini.sh  
  
ENTRYPOINT [ "/usr/bin/tini", "--", "/usr/share/docker/entrypoint.sh" ]  
CMD [ "/bin/bash" ]  

