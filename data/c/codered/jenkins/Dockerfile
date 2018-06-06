FROM codered/ubuntu-java8  
  
MAINTAINER Ronan Gill <ronan.gill@code.red>  
  
ADD http://mirrors.jenkins-ci.org/war-stable/latest/jenkins.war
/u01/jenkins.war  
  
RUN apt-get update && \  
apt-get install -y git-core && \  
groupadd -g 1007 jenkins && useradd -u 1006 -g 1007 -s /sbin/nologin -m
jenkins && \  
chown -R jenkins:users /u01/* && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8080  
VOLUME ["/home/jenkins"]  
USER jenkins  
ENV JENKINS_HOME /home/jenkins  
  
CMD java -jar /u01/jenkins.war --prefix=/jenkins  

