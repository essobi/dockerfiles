FROM centos:7  
MAINTAINER Ding Wen Xiang "624380857@qq.com"  
ADD https://raw.githubusercontent.com/docker-zone/docker-os-sshd/master/run.sh
/run.sh  
  
RUN yum install -y openssh-server \  
&& yum install -y epel-release \  
&& yum install -y pwgen \  
&& mkdir -p /app/tools/sshd \  
&& ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_ecdsa_key \  
&& ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_ed25519_key \  
&& ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key \  
&& chmod +x /run.sh \  
&& yum remove -y epel-release \  
&& yum clean all  
  
EXPOSE 22  
CMD ["/run.sh"]  

