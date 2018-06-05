#------------------------------------------------------------------------------  
# Set the base image for subsequent instructions:  
#------------------------------------------------------------------------------  
  
FROM centos:7  
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>  
  
#------------------------------------------------------------------------------  
# Install:  
#------------------------------------------------------------------------------  
  
RUN rpm --import http://mirror.centos.org/centos/7/os/x86_64/RPM-GPG-KEY-
CentOS-7  
RUN yum update -y && yum clean all  
RUN yum install -y dnsmasq syslinux-tftpboot && yum clean all  
RUN mkdir /tftpboot && \  
ln /var/lib/tftpboot/pxelinux.0 /tftpboot/ && \  
ln /var/lib/tftpboot/menu.c32 /tftpboot/  
ADD rootfs /  
  
#------------------------------------------------------------------------------  
# Entrypoint:  
#------------------------------------------------------------------------------  
  
ENTRYPOINT ["/init", "/usr/sbin/dnsmasq", "-k"]  

