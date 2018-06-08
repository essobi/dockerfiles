FROM centos:latest  
  
MAINTAINER Delaney Burke (aka Cococoder) - Nubibus  
  
# Epel  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
  
# Install Development Tools  
RUN yum -y groupinstall "Development Tools"  
  
# yum update  
RUN yum -y update  
RUN yum clean all  
  
RUN \curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.1.0"  
RUN /bin/bash -l -c "gem install bundler pry pry-remote --no-ri --no-rdoc"  
RUN /bin/bash -l -c "rvm --default use 2.1.0"  

