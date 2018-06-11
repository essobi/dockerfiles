FROM centos:7  
MAINTAINER youyo  
  
ENV VAGRANT_VERSION 1.9.1  
RUN yum install -y
https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.rpm
&& \  
vagrant plugin install vagrant-aws vagrant-digitalocean && \  
vagrant box add dummy https://github.com/mitchellh/vagrant-
aws/raw/master/dummy.box  

