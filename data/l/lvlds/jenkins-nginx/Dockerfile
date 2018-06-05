FROM jenkins:latest  
  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  
ENV JENKINS_OPTS --prefix=/jenkins  
  
EXPOSE 8080

