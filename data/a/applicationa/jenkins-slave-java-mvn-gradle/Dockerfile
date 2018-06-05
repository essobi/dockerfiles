# Ubuntu 14.04.2 LTS  
# Oracle Java 8u40 64 bit  
# Maven 3.3.1  
# Gradle 2.3  
# Git 2.3.5  
# Jenkins Swarm Client 1.22  
# extend the most recent long term support Ubuntu version  
FROM applicationa/jenkins-slave-java-gradle  
  
MAINTAINER Applicationa Deploy (http://applicationa.com,
deploy@applicationa.com)  
  
WORKDIR /data  
  
# install maven  
# http://linuxg.net/how-to-install-git-2-3-4-on-
ubuntu-15-04-ubuntu-14-10-ubuntu-14-04-ubuntu-12-04-and-derivative-systems/  
RUN apt-get purge -y maven maven2 && \  
add-apt-repository ppa:timothy-downey/maven3 && \  
apt-key update && apt-get update && \  
apt-get install -y maven3 && \  
apt-get clean

