FROM ubuntu:14.04  
MAINTAINER knjname  
  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jre-headless  
  
RUN mkdir -p /jenkins/bin  
RUN mkdir -p /jenkins/home  
RUN mkdir -p /jenkins/logs  
  
ADD http://mirrors.jenkins-ci.org/war/1.567/jenkins.war
/jenkins/bin/jenkins.war  
ADD run.sh /jenkins/bin/run.sh  
  
CMD bash /jenkins/bin/run.sh  

