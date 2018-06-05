FROM centos/systemd  
MAINTAINER David LEVRAY <dlevray@gmail.com>  
LABEL version="1.0"  
LABEL description="Base image for the Openstack installation"  
LABEL readme="this image is used as the base for installing all Openstack
components"  
  
RUN yum update -y  
RUN yum install -y yum-plugin-priorities net-tools iputils.x86_64 curl.x86_64
ksh.x86_64 chrony && \  
systemctl enable chronyd.service && \  
yum install -y centos-release-openstack-queens && \  
yum update -y && \  
yum upgrade -y && \  
yum install -y python-openstackclient openstack-selinux && \  
yum clean all  
  
CMD ["/usr/sbin/init"]  

