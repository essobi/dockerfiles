FROM centos:centos5.11  
  
ENV SALT_VERSION=2017.7.0  
  
ADD start.sh /bin/start.sh  
  
RUN rpm --import
http://repo.saltstack.com/yum/redhat/5/x86_64/archive/$SALT_VERSION/SALTSTACK-
EL5-GPG-KEY.pub \  
&& echo -e "[saltstack-repo]\nname=SaltStack repo for
RHEL/CentOS\$releasever\nbaseurl=https://repo.saltstack.com/yum/redhat/\$releasever/\$basearch/archive/$SALT_VERSION\nenabled=1\ngpgcheck=1\ngpgkey=https://repo.saltstack.com/yum/redhat/\$releasever/\$basearch/archive/$SALT_VERSION/SALTSTACK-
EL5-GPG-KEY.pub\n" > /etc/yum.repos.d/saltstack.repo \  
&& yum install -y salt-minion-${SALT_VERSION}* epel-release sudo
policycoreutils selinux-policy-targeted \  
&& mkdir -p /etc/salt/minion.d \  
&& echo -e "master: master" > /etc/salt/minion.d/masters.conf \  
&& sed -i -e 's/#hash_type.*/hash_type: sha256/' /etc/salt/minion \  
# fix for systemd  
&& yum install -y initscripts \  
&& chkconfig salt-minion on \  
  
&& rm -rf /var/lib/yum/* \  
&& yum clean all  
  
ENTRYPOINT ["/bin/start.sh"]  

