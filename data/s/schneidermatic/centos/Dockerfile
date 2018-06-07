#==============================================================================  
# Ported by: Markus Schneider  
# Arch: xv86_64  
# Entities: CentOS-7.2  
# OpenSSH  
#  
# Original Authors:  
#  
# "ported" by Adam Miller <maxamillion@fedoraproject.org> from  
# https://github.com/fedora-cloud/Fedora-Dockerfiles  
#  
# Originally written for Fedora-Dockerfiles by  
# scollier <scollier@redhat.com>  
#  
#==============================================================================  
FROM centos:centos7  
MAINTAINER markus.schneider73@gmail.com  
  
## Set work dir  
WORKDIR /tmp  
  
## Upgrading system  
RUN yum -y upgrade; yum clean all  
RUN yum -y install sudo epel-release; yum clean all  
  
## Enable installation of man pages  
RUN sed -i "s/tsflags=nodocs/#tsflags=nodocs/" /etc/yum.conf  
  
##------------------------------------------------------------------------------  
## BASE INSTALL  
##------------------------------------------------------------------------------  
## Add Tools  
RUN yum -y install wget \  
curl \  
which \  
man \  
man-pages \  
man-pages-overrides \  
passwd \  
git \  
tar \  
unzip \  
sudo \  
gawk \  
sed \  
openssh \  
openssh-server \  
openssh-clients \  
supervisor \  
pwgen \  
python  
  
RUN yum clean all  
  
## Add Scripts  
RUN mkdir -p /opt/docker/scripts  
COPY src/scripts /opt/docker/scripts  
  
## Add Config  
COPY src/config/supervisord.conf /etc/supervisord.conf  
  
## Set work dir  
WORKDIR /opt/docker/scripts  
  
## Run Scripts  
## Set Credentials  
RUN ./setup setCrd  
  
## Add SSH Host Key  
RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
  
## Set SSH Key  
WORKDIR /home/sysadm  
RUN mkdir .ssh  
RUN ssh-keygen -t rsa -b 4096 -C "comment" -P "changeit" -f
"/home/sysadm/.ssh/id_rsa" -q  
RUN chown -R sysadm:sysadm /home/sysadm/.ssh  
RUN chmod -R 700 /home/sysadm/.ssh  
  
## Add .bashrc  
ADD src/scripts/bashrc /home/sysadm/.bashrc  
RUN chmod 644 /home/sysadm/.bashrc  
RUN chown sysadm:sysadm /home/sysadm/.bashrc  
  
## Add ssh* commands  
ADD src/scripts/ssh* /home/sysadm/  
RUN chmod 755 /home/sysadm/ssh*  
RUN chown -R sysadm:sysadm /home/sysadm/ssh*  
  
## Add custom bashrc  
ADD src/scripts/bashrc /home/sysadm/.bashrc  
RUN chmod 744 /home/sysadm/.bashrc  
RUN chown -R sysadm:sysadm /home/sysadm/.bashrc  
  
##------------------------------------------------------------------------------  
## EXPOSED PORTS  
##------------------------------------------------------------------------------  
## -- SSH Port(22)  
EXPOSE 22  
## Run bootstrap script  
CMD ["/bin/bash","/opt/docker/scripts/bootstrap.sh"]  

