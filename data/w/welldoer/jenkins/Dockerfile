FROM ubuntu:14.04  
MAINTAINER welldoer  
ENV REFRESHED_AT 2015-12-06  
RUN apt-get update -qq && apt-get install -qqy wget curl openjdk-7-jdk git  
RUN wget -qO- https://get.docker.com/ | sh  
  
ENV JENKINS_HOME /opt/jenkins/data  
ENV JENKINS_MIRROR http://mirrors.jenkins-ci.org  
  
RUN mkdir -p $JENKINS_HOME/plugins  
RUN curl -sf -o /opt/jenkins/jenkins.war -L $JENKINS_MIRROR/war-
stable/latest/jenkins.war  
  
RUN for plugin in chucknorris greenballs scm-api git-client git ws-cleanup ;\  
do curl -sf -o $JENKINS_HOME/plugins/${plugin}.hpi \  
-L $JENKINS_MIRROR/plugins/${plugin}/latest/${plugin}.hpi ; done  
  
ADD ./dockerjenkins.sh /usr/local/bin/dockerjenkins.sh  
RUN chmod +x /usr/local/bin/dockerjenkins.sh  
  
VOLUME /var/lib/docker  
  
EXPOSE 8080  
ENTRYPOINT [ "/usr/local/bin/dockerjenkins.sh" ]  

