FROM java:8-jdk  
MAINTAINER Sid Zhang <zhangnaixiao@me.com>  
  
# Refresh the package repository  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install git  
RUN apt-get install -y git  
  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
# Add user jenkins to the image  
RUN adduser --quiet jenkins  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Expose user workspace  
VOLUME /home/jenkins  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

