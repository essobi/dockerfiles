FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN printf "GatewayPorts yes\n" >> /etc/ssh/sshd_config  
RUN printf "PermitOpen 0.0.0.0:25\n" >> /etc/ssh/sshd_config  
RUN printf "AllowTcpForwarding yes\n" >> /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/bin/bash","-c","echo 'root:'`cat '/run/secrets/ssh_password'` |
chpasswd && date && '/usr/sbin/sshd' -D"]  

