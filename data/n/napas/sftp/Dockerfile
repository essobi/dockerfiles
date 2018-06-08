FROM ubuntu  
MAINTAINER Mindaugas Mačiulaitis <napas@napas.lt>  
  
# Make sure the package repository is up to date.  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
RUN adduser --quiet sftp  
RUN echo "sftp:sftp" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

