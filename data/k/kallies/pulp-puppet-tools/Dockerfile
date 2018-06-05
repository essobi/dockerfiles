FROM centos:7  
MAINTAINER Lukas Kallies  
  
ADD rhel-pulp.repo /etc/yum.repos.d/  
  
# update the system first, then add epel-release  
RUN yum -y update \  
&& yum -y install epel-release \  
&& yum -y install gem rubygem-bundler puppet pulp-puppet-tools \  
&& yum clean all  

