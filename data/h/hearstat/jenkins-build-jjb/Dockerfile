FROM hearstat/jenkins-build-base:alpine  
  
MAINTAINER Hearst Automation Team "atat@hearst.com"  
ENV JJBVERSION 1.6.1  
RUN sudo apk --update add --no-cache py-pip &&\  
sudo pip install jenkins-job-builder==${JJBVERSION} &&\  
sudo rm -rf /var/cache/apk/* &&\  
sudo rm -rf /tmp/*  
  
CMD ["/usr/sbin/sshd", "-D"]  

