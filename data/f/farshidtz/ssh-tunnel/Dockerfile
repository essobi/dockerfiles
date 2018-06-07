FROM debian:stable-slim  
  
RUN apt update && \  
apt -y install openssh-server  
# RUN apt -y install fail2ban  
RUN mkdir /var/run/sshd  
  
RUN useradd -ms /bin/bash limited  
VOLUME /home/limited/.ssh  
EXPOSE 22  
ENTRYPOINT ["/usr/sbin/sshd"]  

