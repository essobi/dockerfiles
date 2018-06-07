FROM centos:centos6  
  
MAINTAINER andrea.ceccanti@gmail.com  
  
RUN \  
rpm --import http://mirror.centos.org/centos/6/os/x86_64/RPM-GPG-KEY-CentOS-6
&& \  
rpm --import http://mirror.centos.org/centos/6/os/x86_64/RPM-GPG-KEY-CentOS-
Debug-6 && \  
rpm --import http://mirror.centos.org/centos/6/os/x86_64/RPM-GPG-KEY-CentOS-
Testing-6 && \  
rpm --import http://mirror.centos.org/centos/6/os/x86_64/RPM-GPG-KEY-CentOS-
Security-6 && \  
rpm -Uvh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm && \  
yum clean all && \  
yum -y update && \  
yum --enablerepo=centosplus install -y epel-release redhat-lsb wget git tar
puppet && \  
puppet module install \--force maestrodev-wget && \  
puppet module install \--force puppetlabs-stdlib  

