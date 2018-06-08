FROM jenkins:1.651.2  
MAINTAINER Ruben  
  
# Setup log folder  
USER root  
RUN mkdir /var/log/jenkins  
RUN mkdir /var/cache/jenkins  
RUN chown -R jenkins:jenkins /var/log/jenkins  
RUN chown -R jenkins:jenkins /var/cache/jenkins  
USER jenkins  
  
# Set environmental variables  
ENV JAVA_OPTS="-Xmx8192m"  
ENV JENKINS_OPTS="--handlerCountStartup=100 --handlerCountMax=300
--logfile=/var/log/jenkins/jenkins.log --webroot=/var/cache/jenkins/war"  

