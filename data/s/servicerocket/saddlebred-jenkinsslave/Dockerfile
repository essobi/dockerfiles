FROM java:8  
MAINTAINER ServiceRocket Tools  
  
RUN apt-get update && apt-get install -y \  
openssh-server \  
ca-certificates \  
curl \  
apt-transport-https \  
ca-certificates \  
lxc \  
iptables  
  
# Configure SSH as part of Jenkins slave requirement  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

