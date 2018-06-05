#################################################################  
# Dockerfile to build bastion container image  
# Based on CentOS 7  
# Created by Alan Denniston  
#################################################################  
FROM centos:latest  
MAINTAINER Alan Denniston <alan.denniston@gmail.com>  
  
RUN yum install -y epel-release && yum update -y --nogpgcheck && yum install
-y --nogpgcheck \  
wget \  
dialog \  
sqlite \  
dnsmasq \  
bind-utils \  
sudo \  
sysstat \  
unzip \  
ruby \  
rubygems \  
jruby \  
perl \  
perl-core \  
nmap \  
gmp \  
unzip \  
telnet \  
net-tools \  
tmux \  
weechat \  
finch \  
which \  
bc \  
vim-enhanced \  
openssh-server \  
openssh-clients \  
&& yum clean all \  
&& yum clean metadata \  
&& ssh-keygen -A  
# For local builds  
#&& adduser -s /bin/bash myuser \  
#&& echo "myuser:mypass" | chpasswd \  
#&& mkdir -p /home/myuser/.ssh  
  
VOLUME ["/opt/"]  
  
EXPOSE 22  
  
#ADD etc/motd /etc/motd  
  
# For local builds  
#COPY home/myuser /home/myuser/  
#RUN chmod 660 /etc/sudoers && chown -R myuser:myuser /home/myuser && chmod -R
600 /home/myuser/.ssh && chmod +x /home/myuser/bin/*  
  
CMD ["/sbin/sshd", "-D", "-e"]  

