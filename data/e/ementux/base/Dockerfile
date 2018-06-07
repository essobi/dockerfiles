#  
# ementux/base  
#  
# CentOS maintained base image with little adjustment  
#  
# See https://github.com/ementux/docker  
#  
FROM centos:latest  
MAINTAINER Michal Grna <michal.grna@ementux.org>  
  
# define terminal type  
ENV TERM xterm  
  
# import CentOS certificate  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7  
  
# install EPEL repository  
RUN yum -y install epel-release  
  
# import EPEL certificate  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7  
  
# add runit  
COPY runit-2.1.2-1.el7.centos.x86_64.rpm
/tmp/runit-2.1.2-1.el7.centos.x86_64.rpm  
COPY runit_bootstrap /usr/sbin/runit_bootstrap  
RUN chmod 755 /usr/sbin/runit_bootstrap  
  
# update && install runit + some basic utilities && clean stuff after
installation  
RUN yum -y update && yum -y install bash-completion vim-enhanced hostname
bind-utils psmisc /tmp/runit-2.1.2-1.el7.centos.x86_64.rpm && yum clean all  
RUN rm /tmp/runit-2.1.2-1.el7.centos.x86_64.rpm  

