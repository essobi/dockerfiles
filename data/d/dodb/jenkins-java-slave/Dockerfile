FROM java:8-jdk  
MAINTAINER David Op de Beeck <davidopdebeeck@hotmail.com>  
  
# Update repositories  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# SSH  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
# Add the slave user (username: jenkins;password: jenkins) to the system  
RUN adduser --quiet jenkins  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Expose SSH default port  
EXPOSE 22  
# Run ssh server as default  
CMD ["/usr/sbin/sshd", "-D"]  

