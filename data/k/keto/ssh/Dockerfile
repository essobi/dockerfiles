FROM centos:centos7  
  
MAINTAINER Mikael Keto  
  
# add epel repository and gpg key  
ADD epel.repo /etc/yum.repos.d/epel.repo  
ADD RPM-GPG-KEY-EPEL-7 /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7  
  
COPY entrypoint.sh /entrypoint.sh  
  
# install openssh server  
RUN yum -y install openssh-server unison240-text && \  
yum clean all && rm -rf /var/cache/yum && \  
chmod 755 /entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D"]

