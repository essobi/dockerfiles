# Set the base image  
FROM ubuntu:latest  
  
# Dockerfile author / maintainer  
MAINTAINER Julien Coppi <julien.coppi@gmail.com>
https://github.com/itchykun/docker-test  
  
# Add labels... What for?  
# LABEL name="CentOS Base Image" \  
# vendor="CentOS" \  
# license="GPLv2" \  
# build-date="20160906"  
  
# Add a file from Github to a specific folder within the container  
# ADD centos-7-docker.tar.xz /  
  
# Commands to be executed  
RUN apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qy ncdu \  
&& apt-get clean \  
&& rm -rf /var/lib/apt  
  
# No clue what this does :)  
# ENTRYPOINT ["mysql"]  
  
# Launch a command at the end of the build process  
CMD ["/bin/bash"]  

