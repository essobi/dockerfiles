FROM titanous/ubuntu  
  
RUN apt-get update && apt-get install -y openssh-server sudo &&\  
useradd --create-home -s /bin/bash ubuntu &&\  
adduser ubuntu sudo &&\  
echo "ubuntu:ubuntu" | chpasswd &&\  
sed -re "s/PasswordAuthentication\s.*/PasswordAuthentication yes/g" -i
/etc/ssh/sshd_config  
  
ADD id_rsa.pub /home/ubuntu/.ssh/authorized_keys  
RUN chown ubuntu:ubuntu /home/ubuntu/.ssh/authorized_keys && chmod 600
/home/ubuntu/.ssh/authorized_keys && mkdir /var/run/sshd  
  
EXPOSE 22  
CMD ["/sbin/init"]  

