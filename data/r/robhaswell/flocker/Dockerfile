FROM centos:7  
MAINTAINER Rob Haswell <me@robhaswell.co.uk>  
  
#RUN if selinuxenabled; then setenforce 0; fi  
#RUN test -e /etc/selinux/config && sed --in-place='.preflocker'
's/^SELINUX=.*$/SELINUX=disabled/g' /etc/selinux/config  
RUN yum clean all  
RUN yum install --nogpgcheck -y https://clusterhq-
archive.s3.amazonaws.com/centos/clusterhq-release$(rpm -E %dist).noarch.rpm  
RUN yum install --nogpgcheck -y clusterhq-flocker-node  

