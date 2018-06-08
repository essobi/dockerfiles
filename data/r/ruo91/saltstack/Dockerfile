#  
# Title: SaltStack Minion  
#  
# Maintainer: Yongbok Kim (ruo91@yongbok.net)  
#  
# - Build  
# docker build --rm -t saltstack:minion -f 01_saltstack_minion .  
#  
# - Run  
# docker run -d --name="saltstack-minion-1" -h "saltstack-minion-1"
saltstack:minion  
# docker run -d --name="saltstack-minion-2" -h "saltstack-minion-2"
saltstack:minion  
# Base images  
FROM centos:centos6  
MAINTAINER Yongbok Kim <ruo91@yongbok.net>  
  
# EPEL  
RUN rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm \  
&& yum install -y https://repo.saltstack.com/yum/redhat/salt-repo-
latest-1.el6.noarch.rpm  
  
# SaltStack Minion  
RUN yum install -y openssh-clients openssh-server salt-minion \  
&& sed -i '/^#master: salt/ s:.*:master\: saltstack-master:' /etc/salt/minion  
  
# SSH  
ADD conf/ssh_key/authorized_keys /root/.ssh/authorized_keys  
RUN chmod 0644 /root/.ssh/authorized_keys  
RUN sed -i '/^UseLogin/ s:.*:UseLogin yes:' /etc/ssh/sshd_config \  
&& sed -i '/^#PermitRootLogin/ s:.*:PermitRootLogin yes:' /etc/ssh/sshd_config
\  
&& sed -i '/^# StrictHostKeyChecking ask/ s:.*: StrictHostKeyChecking no:'
/etc/ssh/ssh_config  
  
# Supervisor  
RUN yum install -y python-setuptools python-meld3 \  
&& easy_install pip \  
&& pip install --upgrade pip \  
&& pip install supervisor \  
&& mkdir /etc/supervisord.d  
ADD conf/saltstack_minion_supervisord.conf /etc/supervisord.d/supervisord.conf  
  
# Set the root password for ssh  
RUN echo 'root:salt' |chpasswd  
  
# Port  
# SSH: 22  
EXPOSE 22  
# Supervisor  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]  

