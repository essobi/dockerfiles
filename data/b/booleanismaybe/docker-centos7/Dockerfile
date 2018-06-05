FROM centos:7  
ENV container=docker  
  
RUN yum -y update; yum clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
RUN yum makecache fast \  
&& yum -y install deltarpm epel-release initscripts \  
&& yum -y update \  
&& yum -y install \  
ansible \  
sudo \  
which \  
net-tools \  
&& yum clean all  
  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
VOLUME ["/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  

