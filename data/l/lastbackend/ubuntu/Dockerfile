FROM ubuntu:utopic  
  
MAINTAINER team@lastbackend.com  
  
# Install packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
openssh-server pwgen  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i
"s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 22  
CMD ["/init.sh"]

