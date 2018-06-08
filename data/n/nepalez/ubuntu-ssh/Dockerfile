# Ubuntu 14.04 with SSH support  
FROM ubuntu:14.04  
MAINTAINER Andrew Kozin <andrew.kozin@gmail.com>  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages  
RUN apt-get update -qq && \  
apt-get install -y -qq openssh-server && \  
apt-get clean -qq  
  
# Config SSH  
RUN mkdir -p /var/run/sshd && \  
sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \  
sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
# Expose SSH port by default  
EXPOSE 22  

