  
FROM centos:centos7  
  
MAINTAINER "Guy Klainer" <guyk@dauup.com>  
  
ENV container docker  
  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs  
RUN yum -y update; yum clean all; \  
cd /lib/systemd/system/sysinit.target.wants/; \  
for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done; \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
RUN yum -y install vim-X11 vim-common vim-enhanced vim-minimal git wget
mlocate gcc gcc-c++  
RUN updatedb  
  
RUN yum -y install httpd; yum clean all; systemctl enable httpd.service  
RUN yum -y install php php-devel  
  
RUN chkconfig httpd on  
  
CMD ["/usr/sbin/init"]  
  

