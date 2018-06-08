FROM kreczko/centos6  
  
MAINTAINER Luke Kreczko <kreczko@cern.ch>  
  
RUN rpm --import https://yum.puppetlabs.com/RPM-GPG-KEY-puppetlabs  
RUN rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm  
RUN yum -y update  
# setup puppet and hiera  
RUN yum -y install puppet tar git  
ADD hiera.yaml /etc/puppet/hiera.yaml  
RUN mkdir /etc/puppet/hieradata  
ADD common.yaml /etc/puppet/hieradata/common.yaml  
  
# setup site module  
RUN cd /etc/puppet/modules  
RUN git clone https://github.com/uobdic/dice_T2_puppet_config.git site  
RUN cd site && git checkout r10k-dev  

