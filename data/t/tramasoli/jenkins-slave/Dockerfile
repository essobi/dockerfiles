# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM tramasoli/jenkins-slave:base  
MAINTAINER Fábio Tramasoli <fabio@tramasoli.com>  
  
# Install JDK 7,8 (latest edition)  
RUN apt-get update &&\  
apt-get install -y openjdk-7-jdk &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  
# Standard SSH port  
EXPOSE 22  
  
CMD ["/bin/bash","/bootstrap.sh"]

