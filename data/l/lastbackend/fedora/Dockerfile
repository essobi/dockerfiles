FROM fedora:20  
MAINTAINER team@lastbackend.com  
  
# Install packages and set up sshd  
RUN yum -y install openssh-server pwgen && \  
rm -f /etc/ssh/ssh_*_key && \  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key && \  
sed -i "s/#*UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/#*UseDNS.*/UseDNS no/g" /etc/ssh/sshd_config  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 22  
CMD ["/init.sh"]

