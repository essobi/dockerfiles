FROM ubuntu:14.04  
RUN sudo apt-get install -y wget  
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-
key add -  
RUN sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list'  
RUN sudo apt-get update  
RUN sudo apt-get install -y jenkins  
  
EXPOSE 8080  
CMD su jenkins -c 'java -jar /usr/share/jenkins/jenkins.war'  

