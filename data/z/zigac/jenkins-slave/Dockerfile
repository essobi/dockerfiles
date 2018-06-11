# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM ubuntu:xenial  
MAINTAINER Ziga Ciglar <ziga.ciglar@gmail.com>  
  
# Install and configure a basic SSH server  
RUN apt-get update &&\  
apt-get install -y openssh-server &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
# Install JDK 8 (latest edition)  
RUN apt-get update &&\  
apt-get install -y openjdk-8-jdk &&\  
apt-get install -y maven &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  
# Set user jenkins to the image  
RUN adduser --quiet jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Create symbolic link as expected by master jenkins.  
RUN mkdir -p /home/jenkins/opt/jdk1.8.0_5 &&\  
ln -s /usr/lib/jvm/java-8-openjdk-amd64/* /home/jenkins/opt/jdk1.8.0_5  
# Standard SSH port  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  

