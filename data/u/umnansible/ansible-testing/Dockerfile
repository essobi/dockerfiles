FROM centos:centos7  
  
RUN yum -y install \  
epel-release centos-release-scl centos-release-scl-rh \  
dbus libselinux-python python2-devel git python-setuptools python-setuptools-
dev openssl-devel gcc \  
sudo openssh-server openssh-clients which curl htop \  
&& easy_install pip \  
&& pip install -U setuptools \  
&& pip install ansible \  
&& rm -rf ~/.cache \  
&& yum -y remove python2-devel python-setuptools-dev openssl-devel gcc \  
&& yum -y autoremove \  
&& yum clean all  
RUN echo "SSHD_OPTS='-o UseDNS=no -o UsePAM=no -o PasswordAuthentication=yes
-o UsePrivilegeSeparation=no -o PidFile=/tmp/sshd.pid'" > /etc/default/ssh  
RUN systemctl enable sshd.service  
  
CMD ["/usr/sbin/init"]  

