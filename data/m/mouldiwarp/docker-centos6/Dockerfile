# Start with a base centos6 image from centos  
FROM centos:centos6  
  
# Next install epel  
RUN yum install -y man vim tar epel-release  
  
# Run an update on the image  
RUN yum update -y  
  
# Cleanup yum post update  
RUN yum clean all  

