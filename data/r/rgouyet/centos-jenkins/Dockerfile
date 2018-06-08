FROM centos:7  
MAINTAINER Romain Gouyet <github@gouyet.com>  
  
RUN yum -y install java-1.8.0-openjdk git mercurial mc subversion  
  
ENV JENKINS_VERSION 2.46.2  
ENV JENKINS_SHA b91fa09838342980f56224adcf5f02edf668d834  
  
RUN mkdir /opt/jenkins && \  
mkdir -p /opt/data/jenkins/war && \  
curl -fL https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/$JENKINS_VERSION/jenkins-war-$JENKINS_VERSION.war --output
/opt/jenkins/jenkins.jar && \  
echo "$JENKINS_SHA /opt/jenkins/jenkins.jar" | sha1sum -c -  
  
ENV JENKINS_HOME /opt/data/jenkins_home  
  
RUN useradd -d "$JENKINS_HOME" -m -s /bin/bash jenkins  
VOLUME /opt/data/jenkins_home  
  
EXPOSE 8080  
USER jenkins  
  
CMD java -Xms512m -Xmx1024m -jar /opt/jenkins/jenkins.jar  

