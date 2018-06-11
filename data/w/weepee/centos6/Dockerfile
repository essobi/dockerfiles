FROM centos:centos6  
MAINTAINER Gert Van Gool <gert@weepee.org>  
  
RUN cp /etc/yum.repos.d/CentOS-Base.repo{,.bak} && \  
sed 's/^mirrorlist=.*//' /etc/yum.repos.d/CentOS-Base.repo.bak | sed
's/#baseurl=http:\/\/mirror.centos.org\/centos/baseurl=http:\/\/centos.weepee.org/'
> /etc/yum.repos.d/CentOS-Base.repo && \  
rpm -Uvh http://fedora.cu.be/epel/6/i386/epel-release-6-8.noarch.rpm && \  
rpm -Uvh http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm && \  
yum clean all  
RUN yum update -y && yum clean all  

