FROM jenkins/jenkins:latest  
MAINTAINER Brendan Prin  
  
USER root  
run apt-get update  
run apt-get install -y python-pip vim  
run pip install awscli  
  
run cp -r /var/jenkins_home /var/jenkins_home.bak  
run rm -rf /var/jenkins_home/*  
# Testing automated build trigger for branches  

