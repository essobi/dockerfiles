FROM centos:7  
  
MAINTAINER CSA Data Group <csa-data-group@wuxinextcode.com>  
  
# Needed to upgrade Python Pip for the dependencies  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
  
# Dependencies to run tests and add git tags in data_man repo  
RUN yum -y upgrade && \  
yum -y install git python2 python-pip java-1.8.0-openjdk unzip wget which && \  
pip install --upgrade pip && \  
yum -y clean all  
  
ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0

