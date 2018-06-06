FROM alpine:3.5  
MAINTAINER Sean Abbott <sabbott@finmason.comcom>  
  
ENV JENKINS_SWARM_VERSION 3.4  
ENV HOME /home/jenkins  
  
RUN adduser -D jenkins  
RUN apk --update --no-cache add \  
bash \  
curl \  
net-tools \  
openjdk8-jre  
  
RUN curl --create-dirs -sSLo \  
/usr/share/jenkins/swarm-client-$JENKINS_SWARM_VERSION.jar \  
https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION.jar && \  
chmod 755 /usr/share/jenkins  
  
COPY jenkins-swarm-agent.sh /usr/local/bin/jenkins-swarm-agent.sh  
  
USER jenkins  
VOLUME /home/jenkins  
  
ENTRYPOINT ["/usr/local/bin/jenkins-swarm-agent.sh"]  

