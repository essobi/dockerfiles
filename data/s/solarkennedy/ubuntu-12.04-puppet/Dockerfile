FROM ubuntu:precise  
  
RUN apt-get update  
  
# Install upstream puppet  
RUN apt-get install -y wget ca-certificates  
RUN wget --no-check-certificate https://apt.puppetlabs.com/puppetlabs-release-
precise.deb  
RUN dpkg -i puppetlabs-release-precise.deb  
RUN apt-get update  
RUN apt-get -y install puppet  
  
# Per Beaker docs, these are requirements  
# https://github.com/puppetlabs/beaker/wiki/Creating-A-Test-Environment  
RUN apt-get install -y curl ntpdate git ruby  

