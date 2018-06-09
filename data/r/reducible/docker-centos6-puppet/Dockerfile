FROM centos:centos6  
  
RUN rpm --import https://yum.puppetlabs.com/RPM-GPG-KEY-puppetlabs && \  
rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm  
  
RUN yum install yum-utils -y && \  
yum-config-manager --enable centosplus >& /dev/null && \  
yum clean all  
  
ARG VERSION=3.7.3  
RUN yum install -y puppet-${VERSION} && yum clean all  

