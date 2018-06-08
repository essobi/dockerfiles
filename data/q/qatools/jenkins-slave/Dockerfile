FROM dockerfile/java:oracle-java7  
  
MAINTAINER Eroshenko Artem  
  
RUN apt-get update  
  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
RUN adduser --quiet qatools  
RUN echo "qatools:qatools" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
# Install git  
RUN apt-get install -y -q --force-yes git  
ADD build/.gitconfig /home/qatools/.gitconfig  
  
# Change the owner of the home directory  
RUN chown -R qatools:qatools /home/qatools

