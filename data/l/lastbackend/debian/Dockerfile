FROM debian:squeeze  
  
MAINTAINER team@lastbackend.com  
  
# Install centos ssh  
RUN apt-get update && \  
apt-get -y install openssh-server pwgen && \  
mkdir -p /var/run/sshd && \  
sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 22  
CMD ["/init.sh"]

