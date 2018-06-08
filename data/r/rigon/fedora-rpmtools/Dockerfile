# Fedora baseline docker container with RPM tools to create .rpm packages  
# Generated on Sep Aug 12 17:50:51 GMT 2016 using code in this GitHub repo:  
# https://github.com/rigon/docker-fedora-rpmtools  
FROM fedora:latest  
MAINTAINER Ricardo Gonçalves <ricardompgoncalves@gmail.com>  
  
# run script for JDK installation  
RUN dnf -y install rpm-build rpmdevtools  
  
# cleanup image  
RUN dnf clean all  
RUN rm /tmp/*  
  

