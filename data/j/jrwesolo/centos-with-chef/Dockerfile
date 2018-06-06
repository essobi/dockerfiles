FROM centos:latest  
MAINTAINER Jordan Wesolowski <jrwesolo@gmail.com>  
  
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime  
  
# Chaining these commands to reduce layers/size  
RUN yum update -y && \  
yum install -y curl lsof passwd sudo which && \  
yum clean all && \  
yum makecache  
  
RUN curl -L https://www.opscode.com/chef/install.sh | bash  

