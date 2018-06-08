FROM centos:latest  
MAINTAINER Paul Eie "paul@nxtleap.com"  
ENV PUPPET_AGENT_VERSION="1.6.1"  
RUN yum install -y httpd && \  
yum install -y sudo && \  
yum install -y net-tools && \  
yum install -y initscripts  
  
  
RUN rpm -Uvh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm
&& \  
yum upgrade -y && \  
yum update -y && \  
yum install -y puppet-agent-"$PUPPET_AGENT_VERSION" && \  
yum clean all  

