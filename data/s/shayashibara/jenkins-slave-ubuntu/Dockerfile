# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM ubuntu:14.04  
MAINTAINER shayashibara <meikyowise@gmail.com>  
  
RUN apt-get update  
  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
  
# Install JDK 7 (latest edition)  
RUN apt-get install -y --no-install-recommends default-jdk  
  
# Install utilities  
RUN apt-get install -y git wget curl python-virtualenv python-pip build-
essential python-dev  
  
# Add user jenkins to the image  
RUN adduser --quiet jenkins  
  
# Add user jenkins to sudoers with NOPASSWD  
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Setting for sshd  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

