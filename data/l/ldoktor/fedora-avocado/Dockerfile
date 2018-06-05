# This Dockerfile creates an Fedora image with avocado framework installed  
#  
# VERSION 1.1  
FROM fedora  
# based on jpetazzo/dind  
MAINTAINER Lukas Doktor, ldoktor@redhat.com  
# Install and clean in one step to decrease image size  
RUN curl https://avocado-project.org/data/repos/avocado-fedora.repo -o
/etc/yum.repos.d/avocado.repo && dnf install -y python-avocado && dnf clean
all && rm /etc/yum.repos.d/avocado.repo  
CMD avocado  

