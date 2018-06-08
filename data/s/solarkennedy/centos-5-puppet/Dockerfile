FROM tianon/centos:5.9  
# Install upstream puppet  
RUN yum -y install wget  
RUN wget https://yum.puppetlabs.com/el/5/products/x86_64/puppetlabs-
release-5-10.noarch.rpm  
RUN rpm -Uvh puppetlabs-release-5-10.noarch.rpm  
RUN rm puppetlabs-release-5-10.noarch.rpm  
RUN yum -y install puppet  
  
# Per Beaker docs, these are requirements  
# https://github.com/puppetlabs/beaker/wiki/Creating-A-Test-Environment  
RUN yum install -y curl ntp git ruby  

