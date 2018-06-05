FROM ubuntu:14.04  
MAINTAINER Bragra  
  
RUN apt-get update && \  
  
apt-get install -y openssh-server && \  
mkdir /var/run/sshd && \  
  
echo 'root:root' | chpasswd && \  
  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

