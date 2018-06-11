FROM centos:centos7  
MAINTAINER Gregor Schwab <gregor.schwab@uibk.ac.at>  
  
ENV PUPPET_VERSION 1.8.1-1  
RUN rpm --import https://yum.puppetlabs.com/RPM-GPG-KEY-puppetlabs && \  
rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm  
  
RUN yum update -y && yum install yum-utils -y && \  
yum-config-manager --enable centosplus >& /dev/null && \  
yum clean all  
  
RUN yum install -y puppet-agent \  
&& yum clean all && uname -a && cat /etc/redhat-release && export
PATH=/opt/puppetlabs/bin:$PATH && puppet --version  

