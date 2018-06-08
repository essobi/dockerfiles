FROM centos:6.4  
MAINTAINER skarllot@gmail.com  
  
# Adds EPEL repository  
RUN rpm -ivh http://mirror.globo.com/epel/6/i386/epel-release-6-8.noarch.rpm  
RUN rpm --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6  
  
# Pinned to 6.5 version to ensure a more consistent image between builds  
RUN yum clean all  
RUN yum --releasever=6.5 -y update && \  
yum clean all --releasever=6 && \  
yum clean all --releasever=6.5  
  
# Install some useful tools  
RUN yum install -y openssh-clients rsync vim-enhanced nano htop iptraf-ng \  
yum-utils man && \  
yum clean all --releasever=6 && \  
yum clean all --releasever=6.5  
  

