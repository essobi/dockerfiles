# docker build --rm -t tomashavlas/ansible-test:centos7 ansible-test/centos7  
# docker run -it -v /sys/fs/cgroup:/sys/fs/cgroup:ro tomashavlas/ansible-
test:centos7  
FROM tomashavlas/centos7:systemd  
MAINTAINER Tomáš Havlas <tomashavlas@raven-systems.eu>  
  
RUN yum -y install epel-release;\  
yum -y install ansible;\  
yum -y install openssh-clients openssh-server;\  
yum clean all;\  
systemctl enable sshd  
  
EXPOSE 1-65535  
CMD [ "/usr/lib/systemd/systemd" ]  

