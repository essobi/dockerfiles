FROM centos:centos7.3.1611  
  
ENV SALT_VERSION=2017.7.1  
  
ADD start.sh /bin/start.sh  
  
RUN rpm --import
https://repo.saltstack.com/yum/redhat/7/x86_64/archive/$SALT_VERSION/SALTSTACK-
GPG-KEY.pub \  
&& echo -e "[saltstack-repo]\nname=SaltStack repo for
RHEL/CentOS\$releasever\nbaseurl=https://repo.saltstack.com/yum/redhat/\$releasever/\$basearch/archive/$SALT_VERSION\nenabled=1\ngpgcheck=1\ngpgkey=https://repo.saltstack.com/yum/redhat/\$releasever/\$basearch/archive/$SALT_VERSION/SALTSTACK-
GPG-KEY.pub\n" > /etc/yum.repos.d/saltstack.repo \  
&& yum install -y salt-minion-${SALT_VERSION}* salt-master-${SALT_VERSION}*
salt-ssh-${SALT_VERSION}* epel-release sudo policycoreutils selinux-policy-
targeted \  
&& mkdir -p /etc/salt/minion.d \  
&& echo -e "master: master" > /etc/salt/minion.d/masters.conf \  
&& sed -i -e 's/#hash_type.*/hash_type: sha256/' /etc/salt/minion \  
# fix for getty consume 100% cpu  
&& systemctl disable getty@tty1.service \  
  
# fix for systemd  
&& yum install -y initscripts \  
&& chkconfig salt-master on \  
&& chkconfig salt-minion on \  
  
&& rm -rf /var/lib/yum/* \  
&& yum clean all  
  
EXPOSE 4505 4506  
  
ENTRYPOINT ["/bin/start.sh"]  

