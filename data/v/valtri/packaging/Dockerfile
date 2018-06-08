#  
# Based on:  
#  
# * evarga/jenkins-slave:latest  
# * indigo-dc/packaging:bubuntu_latest  
#  
FROM ubuntu:16.04  
MAINTAINER František Dvořák <valtri@civ.zcu.cz>  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# UTF-8 locale  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /var/cache/apt/*.bin  
RUN locale-gen en_US.UTF-8  
  
# ssh, sudo, java - maven default, build tools  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends openssh-server \  
&& apt-get install -y --no-install-recommends sudo \  
&& apt-get install -y --no-install-recommends build-essential gcc git maven
cmake dpkg-dev devscripts debhelper \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /var/cache/apt/*.bin  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd \  
&& mkdir /var/run/sshd  
  
# access for jenkins  
RUN sed -i '/Defaults *requiretty/s/^/#/' /etc/sudoers \  
&& sed -i '/root\tALL=/a jenkins ALL=(ALL) NOPASSWD: ALL' /etc/sudoers  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins \  
&& echo "jenkins:jenkins" | chpasswd  
  
# standard SSH port  
EXPOSE 22  
# default command  
CMD ["/usr/sbin/sshd", "-D"]  

