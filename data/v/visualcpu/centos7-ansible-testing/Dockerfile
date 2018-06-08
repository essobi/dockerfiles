FROM centos:7  
MAINTAINER Dave Kirk <dave@visualcpu.com>  
  
# ensure we have the latest packages  
RUN yum update -y  
RUN yum upgrade -y  
RUN yum clean all  
  
# install / enable systemd  
RUN (cd /lib/systemd/system/sysinit.target.wants/; \  
for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /etc/systemd/system/*.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# install some basic commands to make life easier  
RUN yum install -y curl which sudo deltarpm epel-release initscripts  
  
# install ansible  
RUN yum install -y ansible  
  
# install rvm for acceptance tests  
RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -L get.rvm.io | bash -s stable  
  
RUN /bin/bash -l -c "rvm install 2.1"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
#  
# clean yum  
RUN yum clean all  
  
# disable requiretty  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
# install ansible inventory file.  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
  
VOLUME ["/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  
  
  

