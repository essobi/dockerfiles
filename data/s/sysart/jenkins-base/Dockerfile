FROM java:openjdk-8-alpine  
MAINTAINER jyrki.puttonen@sysart.fi  
RUN adduser -D -H jenkins  
RUN apk update && apk add openssh git  
ADD http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/2.1/swarm-client-2.1-jar-with-dependencies.jar /opt/jenkins/swarm.jar  
WORKDIR /opt/jenkins/  
VOLUME /workspace  
ENTRYPOINT ["java", "-jar", "/opt/jenkins/swarm.jar", "-fsroot", "/workspace"]  

