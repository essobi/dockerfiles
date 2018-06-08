FROM jenkins  
USER root  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y git rsync  
RUN groupadd -g 999 docker  
RUN usermod -a -G docker jenkins  
RUN echo "Europe/Madrid" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
USER jenkins  
COPY jenkins-material-theme.css /var/jenkins_home/userContent/jenkins-
material-theme.css  
#RUN mkdir apps  

