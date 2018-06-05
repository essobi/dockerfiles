FROM centos:7  
MAINTAINER Andrew Kennedy "grkvlt@apache.org"  
# CONTAINER_SERVICE_VERSION_BELOW  
LABEL version="2.0.0-SNAPSHOT"  
  
# setup root account with temporary password (optionally overridden in docker-
entrypoint.sh)  
RUN echo 'root:p4ssw0rd' | chpasswd  
  
# install sshd and other frequently used packages  
RUN yum -y install openssh-server which sudo; \  
mkdir /var/run/sshd ; \  
chmod 600 /var/run/sshd  
  
# create host keys if absent  
RUN if [ -f "/etc/ssh/ssh_host_dsa_key" -a -f "/etc/ssh/ssh_host_rsa_key" ] ;
then \  
echo "SSH host private keys already exists" ; \  
else \  
ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa ; \  
ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa ; \  
fi  
  
# configure sshd to allow login  
RUN sed -i.bk 's/PermitRootLogin.*$/PermitRootLogin yes/g'
/etc/ssh/sshd_config ; \  
echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config; \  
echo 'RSAAuthentication yes' >> /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd || true  
  
COPY docker-entrypoint.sh /  
RUN chmod 700 /docker-entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/docker-entrypoint.sh"]  

