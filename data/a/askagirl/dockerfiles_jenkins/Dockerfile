FROM askagirl/jdk7  
MAINTAINER Fritz Lee "https://github.com/askagirl"  
RUN echo deb http://archive.ubuntu.com/ubuntu saucy main universe >
/etc/apt/sources.list  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo
apt-key add -  
RUN echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list  
RUN apt-get update  
RUN apt-get install jenkins -y  
  
EXPOSE 8080  

