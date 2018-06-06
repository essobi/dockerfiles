# Docker Image for Jenkins Continuous Integration  
FROM ubuntu:latest  
MAINTAINER James Mills, prologic at shortcircuit dot net dot au  
  
RUN apt-get update  
RUN apt-get -y install wget  
  
RUN apt-get install -q -y openjdk-7-jre-headless && apt-get clean  
  
RUN echo "deb http://pkg.jenkins-ci.org/debian binary/" >
/etc/apt/sources.list.d/jenkins.list  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN apt-get update  
  
VOLUME /var/lib/jenkins  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y jenkins  
  
ENV JENKINS_HOME /var/lib/jenkins  
  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
EXPOSE 8000  
CMD ["/usr/local/bin/run"]  

