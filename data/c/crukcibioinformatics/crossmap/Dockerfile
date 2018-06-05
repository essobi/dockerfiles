FROM centos:7  
MAINTAINER Matt Eldridge "matthew.eldridge@cruk.cam.ac.uk"  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum -y update  
  
RUN yum groupinstall -y 'development tools'  
  
RUN yum install -y python-devel  
RUN yum install -y python-pip  
  
RUN yum install -y lzo-devel  
  
RUN pip install CrossMap  
  

