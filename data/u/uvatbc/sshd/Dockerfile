FROM uvatbc/ubuntu:16.04  
RUN sudo apt-get update && \  
sudo apt-get install -y \  
openssh-client \  
openssh-server \  
supervisor \  
wget  
  
RUN /usr/bin/ssh-keygen -b 4096 -f ~/.ssh/id_rsa -N '' && \  
sudo mkdir -p /var/run/sshd  
  
COPY supervisord.conf /etc/supervisor/  
COPY sshd.conf /etc/supervisor/conf.d/  
CMD ["sudo", "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

