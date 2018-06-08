FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y openjdk-8-jdk curl wget git  
ENV HOME /home/jenkins  
  
RUN groupadd -g 1101 jenkins  
RUN useradd -c "Jenkins user" -d $HOME -u 1101 -g 1101 -m jenkins  
  
ARG VERSION=3.5  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
USER jenkins  
RUN mkdir /home/jenkins/.jenkins  
VOLUME /home/jenkins/.jenkins  
WORKDIR /home/jenkins

