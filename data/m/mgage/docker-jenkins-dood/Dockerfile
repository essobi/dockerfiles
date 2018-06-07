# vim: ft=dockerfile  
###############################################################################  
# Jenkins with DooD (Docker outside of Docker)  
# http://github.com/axltxl/docker-jenkins-dood  
# Author: Alejandro Ricoveri <me@axltxl.xyz>  
# Based on:  
# * http://container-solutions.com/2015/03/running-docker-in-jenkins-in-docker  
# * http://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci  
###############################################################################  
  
FROM mgage/ecs-jenkins  
MAINTAINER the internet  
  
ENV docker_version 1.11.2  
# Install necessary packages  
USER root  
ADD ./git-lfs_1.4.4_amd64.deb /git-lfs_1.4.4_amd64.deb  
RUN apt-get update &&\  
apt-get install -y sudo &&\  
dpkg -i /git-lfs_1.4.4_amd64.deb &&\  
apt-get install -f &&\  
curl -sSL https://get.docker.com/ | sh &&\  
apt-get purge -y docker-engine &&\  
apt-get install docker-engine=${docker_version}-0~jessie &&\  
rm -rf /var/lib/apt/lists/*  
  
# Install initial plugins  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
RUN mkdir "$JENKINS_HOME"/.ssh && ssh-keyscan -t rsa github.com >>
"$JENKINS_HOME"/.ssh/known_hosts  
CMD /usr/local/bin/jenkins.sh  

