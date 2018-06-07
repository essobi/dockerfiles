FROM ubuntu:trusty  
  
MAINTAINER Hearst Automation Team "atat@hearst.com"  
# Environment Variables  
ENV JENKINS_HOME /var/lib/jenkins  
  
RUN apt-get update &&\  
apt-get install -y openssh-server \  
git \  
bash \  
openjdk-7-jdk &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
# Add user and group jenkins to the image  
RUN useradd -m -d $JENKINS_HOME -s /bin/bash -U jenkins && \  
echo "jenkins:jenkins" | chpasswd  
  
# Volumes  
VOLUME /var/lib/jenkins  
# Standard SSH port  
EXPOSE 22  
# Downgrade User  
USER jenkins  
  
# Set directory, install gemfile  
WORKDIR $JENKINS_HOME  
  
RUN /usr/bin/ssh-keygen -A  
  
USER root  
#Run ssh to connect  
CMD ["/usr/sbin/sshd", "-D"]  

