FROM centos:7  
MAINTAINER Philipp Schmitt <philipp@schmitt.co>  
  
ADD https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.rpm
/tmp/vagrant.rpm  
  
RUN yum update && yum install -y \  
make gcc gem ruby-devel libvirt-devel openssh-clients && \  
yum clean all && \  
rpm -Uvh /tmp/vagrant.rpm && \  
vagrant plugin install vagrant-proxmox && \  
vagrant plugin install vagrant-libvirt  
  
WORKDIR "/data"  
  
VOLUME ["/mnt/data"]  
  
ENTRYPOINT ["/usr/bin/vagrant"]  

