FROM ubuntu:16.04  
LABEL Author="Christian Wiedemann"  
  
# Make sure the package repository is up to date.  
RUN apt-get update  
RUN apt-get install -y git  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
USER root  
  
  
  
# guide from https://docs.docker.com/engine/installation/linux/docker-
ce/ubuntu/#set-up-the-repository  
RUN apt-get remove docker docker-engine docker.io  
RUN apt-get update && apt-get install -y apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common \  
sudo  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN apt-key fingerprint 0EBFCD88  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
  
RUN apt-get update && apt-get install -y docker-ce  
  
# Add user jenkins to the image  
RUN adduser --quiet jenkins  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
  
RUN mkdir /home/jenkins/.m2  
  
# ADD settings.xml /home/jenkins/.m2/  
RUN chown -R jenkins:jenkins /home/jenkins/.m2/  
  
RUN usermod -aG sudo jenkins  
  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd" "-D"]  

