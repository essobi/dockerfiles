FROM centos  
  
# Install upstream puppet  
RUN rpm -ivh https://yum.puppetlabs.com/el/6/products/x86_64/puppetlabs-
release-6-7.noarch.rpm  
RUN yum -y install puppet  
  
# Per Beaker docs, these are requirements  
# https://github.com/puppetlabs/beaker/wiki/Creating-A-Test-Environment  
RUN yum install -y curl ntp git ruby  

