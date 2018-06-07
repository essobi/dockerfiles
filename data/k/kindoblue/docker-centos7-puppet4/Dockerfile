FROM centos:7  
MAINTAINER kindoblue <kindoblue@gmail.com>  
  
RUN yum -y update  
RUN yum -y upgrade  
  
RUN groupadd -r puppet && useradd -r -g puppet puppet  
  
# install puppet server  
RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm  
RUN yum -y install puppetserver  
ADD puppet.conf /etc/puppetlabs/puppet/puppet.conf  
  
VOLUME ["/opt/puppetlabs/code"]  
  
EXPOSE 8140  
ENTRYPOINT [ "/opt/puppetlabs/bin/puppet", "master", "--no-daemonize", "--
verbose" ]  

