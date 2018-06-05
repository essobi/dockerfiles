FROM alpine:latest  
MAINTAINER atomney <atomney+docker@gmail.com>  
RUN apk add --no-cache openssh bash wget curl && \  
sed -i 's/\#PubkeyAuthentication\ yes/PubkeyAuthentication\ yes/'
/etc/ssh/sshd_config && \  
sed -i 's/\#PasswordAuthentication\ yes/PasswordAuthentication\ no/'
/etc/ssh/sshd_config && \  
sed -i 's/\#PermitEmptyPasswords\ no/PermitEmptyPasswords\ no/'
/etc/ssh/sshd_config && \  
sed -i 's/\#X11Forwarding\ no/X11Forwarding\ yes/' /etc/ssh/sshd_config && \  
sed -i 's/\#AllowTcpForwarding\ yes/AllowTcpForwarding\ yes/'
/etc/ssh/sshd_config && \  
sed -i 's/\#AllowAgentForwarding\ yes/AllowAgentForwarding\ yes/'
/etc/ssh/sshd_config && \  
sed -i 's/\#UseDNS\ no/UseDNS\ no/' /etc/ssh/sshd_config && \  
ssh-keygen -A && \  
adduser -s /bin/bash -S bastion && \  
echo "bastion:bastion" | chpasswd && \  
mkdir -p /home/bastion/.ssh  
  
ADD authorized_keys /home/bastion/.ssh/authorized_keys  
ADD bastion.txt /etc/motd  
ADD where.sh /where.sh  
ADD start.sh /start.sh  
  
RUN chown -R bastion /home/bastion/.ssh && \  
chmod +x /where.sh && \  
chmod +x /start.sh && \  
chmod -R 700 /home/bastion/.ssh && \  
chmod 600 /home/bastion/.ssh/authorized_keys  
  
EXPOSE 22  
#ENTRYPOINT ["/usr/sbin/sshd","-D","-e"]  
CMD ["/start.sh"]  

