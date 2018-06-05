# based on https://docs.docker.com/engine/examples/running_ssh_service/  
FROM ubuntu:14.04  
MAINTAINER Baptiste Mathus <batmat@batmat.net>  
  
RUN apt-get update && \  
apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN mkdir /root/.ssh && \  
wget https://github.com/batmat.keys --output-document
/root/.ssh/authorized_keys  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

