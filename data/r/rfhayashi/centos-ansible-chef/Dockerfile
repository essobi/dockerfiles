FROM centos:centos7  
  
RUN yum -y install epel-release && yum -y install ansible  
  
RUN yum -y install wget && \  
wget
"https://packages.chef.io/files/stable/chef/12.16.42/el/7/chef-12.16.42-1.el7.x86_64.rpm"
&& \  
yum -y install chef-12.16.42-1.el7.x86_64.rpm && \  
rm chef-12.16.42-1.el7.x86_64.rpm  
  
RUN yum clean all

