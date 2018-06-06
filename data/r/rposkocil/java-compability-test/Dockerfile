############################################################  
# Dockerfile to prepare special environment  
# java-combatibility-test  
# for testing app on different versions of java  
############################################################  
  
# IMAGE CONTENT  
# - latest jenkins  
# - plugin updated 2016/02/06  
# - added GitHub plugin  
# - latest java 7 and 8  
  
# Set the base image to Jenkins  
FROM jenkins  
  
# File Maintainer  
MAINTAINER Exprow  
  
# INSTALLING MORE TOOLS  
USER root  
RUN apt-get update -y  
RUN apt-get install -y openjdk-7-jdk  
USER jenkins

