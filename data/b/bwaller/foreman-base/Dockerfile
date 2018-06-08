FROM centos:centos6  
  
MAINTAINER B Waller bjorn@waller.nu  
  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm && \  
yum -y update && \  
yum -y install centos-release-SCL  
  
RUN yum -y install http://yum.theforeman.org/releases/1.9/el6/x86_64/foreman-
release.rpm && \  
yum -y install ruby193-ruby \  
ruby193-rubygems \  
foreman-installer \  
foreman-proxy \  
puppet-server \  
foreman-cli \  
mod_passenger \  
mod_ssl \  
foreman-postgresql \  
foreman-vmware \  
foreman-libvirt \  
ruby193-rubygem-foreman_setup \  
ruby193-rubygem-foreman_host_rundeck \  
ruby193-rubygem-foreman_templates \  
ruby193-rubygem-passenger-native \  
ruby193-rubygem-foreman_bootdisk  
  

