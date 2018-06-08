FROM ubuntu:latest  
  
RUN apt-get update; \  
apt-get -y install ssh sshpass vim  
  
RUN mkdir /var/run/sshd  
  
RUN useradd -ms /bin/bash sshuser  
RUN echo 'sshuser:sshpass' | chpasswd  
RUN usermod -aG sudo sshuser  
RUN echo "sshuser ALL=(ALL:ALL) ALL" >> /etc/sudoers  
  
COPY ./create_ssh_tunnel.sh /create_ssh_tunnel.sh  
RUN chmod 700 /create_ssh_tunnel.sh  
  
ENTRYPOINT /create_ssh_tunnel.sh  
  

