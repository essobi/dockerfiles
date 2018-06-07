FROM openjdk:8-jdk-alpine  
  
MAINTAINER Hearst Automation Team "atat@hearst.com"  
  
ENV JENKINS_HOME /var/lib/jenkins  
  
RUN apk --update add \  
sudo \  
bash \  
git \  
openssh &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /tmp/* &&\  
mkdir -p $JENKINS_HOME/.weechat &&\  
addgroup jenkins &&\  
adduser -h $JENKINS_HOME -D -s /bin/bash -G jenkins jenkins &&\  
chown -R jenkins:jenkins $JENKINS_HOME &&\  
echo "jenkins:jenkins" | chpasswd &&\  
echo "%jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
VOLUME /var/lib/jenkins  
  
EXPOSE 22  
  
WORKDIR /var/lib/jenkins  
  
RUN /usr/bin/ssh-keygen -A  
  
CMD ["sudo", "/usr/sbin/sshd", "-D"]  

