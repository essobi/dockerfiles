FROM fabric8/java-centos-openjdk8-jdk:latest  
MAINTAINER Roger Ding  
  
ENV HOME /home/jenkins  
RUN groupadd -g 10000 jenkins  
RUN useradd -c "Jenkins user" -d $HOME -u 10000 -g 10000 -m jenkins  
LABEL Description="This is a base image, which provides the Jenkins agent
executable (slave.jar)" Vendor="Jenkins project" Version="3.14"  
  
ARG VERSION=3.14  
ARG AGENT_WORKDIR=/home/jenkins/agent  
  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
USER jenkins  
ENV AGENT_WORKDIR=${AGENT_WORKDIR}  
RUN mkdir /home/jenkins/.jenkins && mkdir -p ${AGENT_WORKDIR}  
  
VOLUME /home/jenkins/.jenkins  
VOLUME ${AGENT_WORKDIR}  
WORKDIR /home/jenkins  

