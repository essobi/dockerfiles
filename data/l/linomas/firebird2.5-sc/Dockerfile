FROM centos:centos7  
MAINTAINER Thomas Gruschwitz <gruschwitz.thomas@gmail.com>  
  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY* && \  
yum -y install epel-release && \  
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY* && \  
yum -y upgrade && \  
yum -y install firebird-superclassic && \  
yum -y clean all  
  
ADD ./aliases.conf /etc/firebird/aliases.conf  
  
VOLUME ["/var/lib/firebird/data/"]  
  
EXPOSE 3050  
CMD "/usr/sbin/fbguard"  
  

