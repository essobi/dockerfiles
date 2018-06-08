FROM centos:6.6  
MAINTAINER Shinya Kinoshita <skinoshita@repositories.jp>  
  
LABEL name="CentOS 6.6 Image" \  
description="The image for creating docker container of CentOS 6.6 that has
some necessary packages." \  
distribution="centos" \  
centos-version="6.6" \  
vendor="REPOSITORY <http://www.repositories.jp>" \  
license="MIT"  
  
USER root  
WORKDIR /root  
  
# Add epel repository.  
RUN yum install -y epel-release  
  
# Install necessary packages.  
RUN yum install -y wget \  
curl \  
which \  
initscripts \  
tar \  
bzip2 \  
bzip2-devel \  
gcc \  
gcc-c++ \  
passwd \  
sudo \  
git \  
autoconf \  
vim \  
openssh-server \  
rsync \  
yum-cron \  
yum-utils \  
rpmdevtools  
  
# Reset root's password.  
RUN passwd -d root  
  
# Configure ssh.  
RUN sed -ri 's/^#PermitEmptyPasswords no/PermitEmptyPasswords yes/'
/etc/ssh/sshd_config && \  
sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \  
/usr/bin/ssh-keygen -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N "" && \  
/usr/bin/ssh-keygen -t dsa -b 1024 -f /etc/ssh/ssh_host_dsa_key -N ""  
  
# Configure container.  
EXPOSE 22  
USER root  
WORKDIR /root  
  
CMD ["/usr/sbin/sshd", "-D"]  

