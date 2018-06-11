FROM ubuntu:xenial  
MAINTAINER Alexandre Chaussier <a.chaussier@infopen.pro>  
  
# Setting for packages installation  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install openssh and lsb-release  
RUN apt-get update && \  
apt-get install -y openssh-server=1:7.2* lsb-release=9.20160110 \  
net-tools=1.60* iproute2=4.3.0-1ubuntu3  
  
# Setting the loginuid process attribute become optional  
RUN sed -i 's/^(session\s+)required(\s+pam_loginuid.so)$/$1optional$2/g' \  
/etc/pam.d/sshd  
  
# Ensure directory to store sshd pid exists  
RUN mkdir -p /var/run/sshd  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

