FROM jenkins/jenkins:latest  
USER root  
RUN apt-get update  
RUN apt-get install -y sudo  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
RUN wget
https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz
-O docker.tgz  
RUN tar -xvzf docker.tgz  
RUN mv docker/* /usr/bin/ && chmod +x /usr/bin/docker  
  
# don't forget to mount /var/log/jenkins, /var/run/docker.sock, /var/jenkins
and /var/jenkins_home  

