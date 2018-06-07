FROM centos:centos5  
  
MAINTAINER team@lastbackend.com  
  
# Install centos ssh  
RUN yum -y install openssh-server epel-release pwgen && \  
yum -y install pwgen && \  
rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 22  
CMD ["/init.sh"]

