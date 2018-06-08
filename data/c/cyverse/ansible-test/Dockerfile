FROM centos:7  
# Install systemd -- See https://hub.docker.com/_/centos/  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs  
RUN yum -y update; yum clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /etc/systemd/system/*.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# Install Ansible  
RUN yum groupinstall -y "development tools"  
RUN yum -y install epel-release git sudo python-devel python-setuptools
python-crypto openssl-devel openssl  
RUN easy_install pip  
RUN pip install httplib2 ansible  
  
# Disable requiretty  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
# Install Ansible inventory file  
RUN if [ ! -d "/etc/ansible" ]; then mkdir /etc/ansible; fi  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
  
VOLUME ["/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  

