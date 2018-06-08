FROM centos:7  
  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
COPY ansible.repo /etc/yum.repos.d/ansible.repo  
  
RUN yum --disableplugin=fastestmirror -y install epel-release \  
&& yum --disableplugin=fastestmirror -y install ansible initscripts sudo
cronie \  
&& yum -y update \  
&& rm -rf /var/cache/yum  
  
RUN sed -i 's/Defaults requiretty/Defaults !requiretty/g' /etc/sudoers  
  
RUN echo '# BLANK FSTAB' > /etc/fstab  
# Install Ansible inventory file.  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
  
VOLUME ["/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  

