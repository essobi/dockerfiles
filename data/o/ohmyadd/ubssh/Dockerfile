FROM ubuntu  
  
COPY dist /root/dist  
RUN apt update && \  
apt install -y openssh-server && \  
rm -rf /var/cache/ && \  
rm /etc/ssh/sshd_config && \  
echo "root:root" | chpasswd && \  
mv /root/dist/sshd_config /etc/ssh/sshd_config && \  
mkdir /var/run/sshd && \  
rm -rf /root/dist  
  
CMD /usr/sbin/sshd -D  

