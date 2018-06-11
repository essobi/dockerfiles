FROM centos:latest  
MAINTAINER Ilya Otyutskiy <ilya.otyutskiy@icloud.com>  
RUN yum update -y  
  
# Install EPEL  
RUN yum install -y http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install IUS  
RUN yum install -y
http://dl.iuscommunity.org/pub/ius/stable/Redhat/6/x86_64/ius-
release-1.0-11.ius.el6.noarch.rpm  
  
# Install vortex  
RUN yum install -y http://vortex-rpm.org/el6/noarch/vortex-
release-6-1.vortex.el6.noarch.rpm  
  
# Purge stuff  
RUN yum clean all  
RUN DIRS="/tmp /var/lib/yum/history /var/log /var/tmp" && for i in $DIRS ; do
rm -rf ${i}/* ; done  

