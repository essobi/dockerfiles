FROM centos:centos6  
MAINTAINER thangnvbkhn@gmail.com  
  
# yum で python-pip を入れるために EPEL をインストールしておく  
RUN yum -y install epel-release openssh-server git curl wget vim  
  
# root ユーザでログインできるようにする  
RUN sed -ri 's/^#PermitRootLogin yes/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# root ユーザのパスワードを 'root' にする  
RUN echo 'root:root' | chpasswd  
  
# 使わないにしてもここに公開鍵を登録しておかないとログインできない  
RUN ssh-keygen -t rsa -N "" -f /etc/ssh/ssh_host_rsa_key  
  
# sshd: 22, httpd: 80 を公開する  
EXPOSE 22 80 443 888  
CMD ["/usr/sbin/sshd", "-D"]  

