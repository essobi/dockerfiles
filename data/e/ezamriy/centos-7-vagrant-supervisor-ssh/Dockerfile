FROM centos:centos7  
  
MAINTAINER Eugene Zamriy <eugene@zamriy.info>  
  
ENV LANG en_US.UTF-8  
  
RUN yum -y install http://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
yum -y update && \  
yum -y install openssh-clients openssh-server sudo supervisor && \  
yum clean all && \  
sed -i -e '/\[epel\]/,/^\[/s/enabled=1/enabled=0/' /etc/yum.repos.d/epel.repo
&& \  
ssh-keygen -b 1024 -t rsa -f /etc/ssh/ssh_host_key && \  
ssh-keygen -b 1024 -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -b 1024 -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
sed -i -e 's/^\(AcceptEnv LANG.*\)/\#\1/' -e 's/^\(AcceptEnv LC_.*\)/\#\1/' -e
's/^\(AcceptEnv XMODIFIERS.*\)/\#\1/' /etc/ssh/sshd_config && \  
groupadd -g 1666 vagrant && \  
useradd -g vagrant -u 1666 -d /home/vagrant -m vagrant && \  
echo vagrant | passwd --stdin vagrant && \  
mkdir -m 0700 -p /home/vagrant/.ssh && \  
curl
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub >>
/home/vagrant/.ssh/authorized_keys && \  
chmod 600 /home/vagrant/.ssh/authorized_keys && \  
chown -R vagrant:vagrant /home/vagrant/.ssh && \  
sed -i 's/^\(Defaults.*requiretty\)/#\1/' /etc/sudoers && \  
echo "vagrant ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22 80 443  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

