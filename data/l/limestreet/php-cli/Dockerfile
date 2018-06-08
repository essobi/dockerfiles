#
------------------------------------------------------------------------------  
# Docker provisioning script for the docker web server stack  
#  
# e.g. docker build -t  
#
------------------------------------------------------------------------------  
#
------------------------------------------------------------------------------  
# Start with the official Ubuntu:latest base image  
#
------------------------------------------------------------------------------  
FROM ubuntu:xenial  
  
# Set correct environment variables  
ENV DEBIAN_FRONTEND noninteractive  
  
#
------------------------------------------------------------------------------  
# Provision the server  
#
------------------------------------------------------------------------------  
RUN mkdir /provision  
ADD provision /provision  
RUN chmod +x provision/provision.sh  
RUN provision/provision.sh  
  
#
------------------------------------------------------------------------------  
# Set locale (support UTF-8 in the container terminal)  
#
------------------------------------------------------------------------------  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
#RUN apt-get update && apt-get -y install nginx  
#ENTRYPOINT ["docker-entrypoint.sh"]  
#CMD ["apache2-foreground"]  
CMD ["nginx", "-g", "daemon off;"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

