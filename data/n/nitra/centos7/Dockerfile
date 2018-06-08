FROM centos  
MAINTAINER Nitra <info@nitra.ua>  
#ENV container docker  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum -y update && yum install -y ntp mc vim wget initscripts rootfiles file
openssh-clients  
RUN rm -rf /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Kiev
/etc/localtime  
RUN systemctl enable ntpd  
VOLUME [ "/sys/fs/cgroup" ]  
CMD ["/usr/sbin/init"]  
  

