#  
# CentOS Dockerfile  
#  
# https://bitbucket.org/housesimple/docker-centos  
#  
FROM centos:7  
MAINTAINER Olly Nevard <olly.nevard@housesimple.com>  
  
# Add imeyer/runit packagecloud.io repo.  
ADD runit.repo /etc/yum.repos.d/runit.repo  
  
# Install epel-release and runit.  
RUN yum -y install epel-release runit && \  
yum clean all  
  
# Define default command.  
CMD ["/bin/bash"]  

