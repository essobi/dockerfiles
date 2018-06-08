FROM centos:7  
MAINTAINER "corux"  
ENV container docker  
  
RUN curl --silent -O
https://repo.saltstack.com/yum/redhat/7/x86_64/latest/SALTSTACK-GPG-KEY.pub; \  
rpm --import SALTSTACK-GPG-KEY.pub; \  
rm -f SALTSTACK-GPG-KEY.pub; \  
curl --silent https://repo.saltstack.com/yum/redhat/7/x86_64/saltstack-
rhel7.repo -o /etc/yum.repos.d/saltstack.repo; \  
yum -y install salt-minion; \  
systemctl enable salt-minion.service; \  
curl --silent -L https://www.getchef.com/chef/install.sh | sh; \  
yum -y install iproute less which file policycoreutils sudo openssh-server
openssh-clients; \  
yum -y update; \  
yum clean all; \  
rm -rf /var/cache/yum;  
  
VOLUME [ "/sys/fs/cgroup", "/run", "/tmp" ]  
CMD [ "/usr/sbin/init" ]  

