FROM centos:centos7.4.1708  
  
ENV container=docker  
  
RUN yum install -y epel-release sudo \  
# fix for bad locales setup - https://github.com/CentOS/sig-cloud-instance-
images/issues/71  
&& localedef -i en_US -f UTF-8 C.UTF-8 \  
# install ssh  
&& yum install -y openssh-server which openssh-clients cronie \  
&& echo 'root:root123' | chpasswd \  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& systemctl enable sshd \  
&& touch /etc/selinux/config \  
# fix for systemd  
&& yum install -y initscripts \  
# fix for getty consume 100% cpu  
&& systemctl disable getty@tty1.service \  
&& rm -f /lib/systemd/system/multi-user.target.wants/getty.target \  
# fix for stderr: no crontab for root  
&& echo '# no crontab for root yet' | crontab - \  
# upgrade all  
&& yum -y update \  
# cleanup  
&& rm -rf /var/lib/yum/* /var/cache/yum \  
&& yum clean all  
  
ENTRYPOINT ["/usr/sbin/init"]  

