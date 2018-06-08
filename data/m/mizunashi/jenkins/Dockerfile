FROM jenkins:latest  
MAINTAINER Mizunashi Mana <mizunashi_mana@mma.club.uec.ac.jp>  
  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
COPY custom.groovy /usr/share/jenkins/ref/init.groovy.d/custom.groovy  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt  

