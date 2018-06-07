FROM centos:7  
ADD assets/minit /bin/minit  
ADD assets/startup /etc/minit/startup  
  
ENV TERM=xterm  
  
RUN chmod 700 /etc/minit/startup && yum install -y wget sudo openssh-server
openssh-clients nano rsync && sshd-keygen && ssh-keygen -f /root/.ssh/id_rsa
-t rsa -N ''  
  
ENTRYPOINT ["/bin/minit"]  

