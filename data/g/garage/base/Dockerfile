# -------------------------------------------------------------------  
# $ docker build -t garage/base git://https://github.com/juniorz/garage-
env.git  
# -------------------------------------------------------------------  
FROM stackbrew/ubuntu:saucy  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
# User  
RUN groupadd --gid 9999 garage &&\  
useradd --uid 9999 --gid 9999 --comment "Garage" garage &&\  
usermod -L garage &&\  
mkdir -p /home/garage  
  
# Build tools  
ADD garage /var/garage/  
RUN chgrp -R garage /var/garage  
  
# Base apps  
RUN /var/garage/install curl ca-certificates  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/garage"]  
WORKDIR /garage  
  
# It is causing problems to switch  
# between using executable as CMD or ENTRYPOINT at `docker run`  
# CMD ["/var/garage/info", "--help"]

