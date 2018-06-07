FROM centos:centos7  
MAINTAINER Igor Gnatenko <i.gnatenko.brain@gmail.com>  
ENV container docker  
# update system  
RUN yum -y update; yum clean all  
  
# systemd fix  
RUN \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
  
# enable my repo with itop-itsm  
RUN curl https://copr.fedoraproject.org/coprs/ignatenkobrain/itop-
itsm/repo/epel-7/ignatenkobrain-itop-itsm-epel-7.repo -o \  
/etc/yum.repos.d/_copr_ignatenkobrain-itop-itsm.repo  
# enable EPEL repo  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-
release-7-0.2.noarch.rpm; yum clean all  
# install itop-itsm  
RUN yum -y install itop-itsm; yum clean all  
# configure mariadb  
ADD cfgmariadb.sh /tmp/  
RUN chmod +x /tmp/cfgmariadb.sh  
USER mysql  
RUN /tmp/cfgmariadb.sh  
USER root  
RUN rm /tmp/cfgmariadb.sh  
# enable httpd and mariadb  
RUN systemctl enable httpd mariadb  
# disable avahi  
RUN systemctl disable avahi-daemon  
  
EXPOSE 80  
CMD ["/usr/sbin/init"]  

