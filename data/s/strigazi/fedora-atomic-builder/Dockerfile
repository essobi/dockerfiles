# This is a utility image to use rpm-ostree and diskimage-builder.  
#  
# The main reason is that it pulls ~400 packages, so it's MUCH faster  
# to keep it in a pre-cooked image.  
FROM fedora:rawhide  
MAINTAINER Spyros Trigazis <strigazi@gmail.com>  
  
ENV container=docker  
USER root  
  
RUN dnf install -y \  
@development-tools \  
createrepo \  
kpartx \  
git \  
python-backports-lzma \  
python-devel \  
python-pip \  
python-yaml \  
sudo \  
rpm-build \  
rpm-ostree-toolbox \  
@virtualization \  
yum \  
yum-utils \  
curl \  
wget  

