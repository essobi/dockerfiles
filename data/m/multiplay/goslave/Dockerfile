FROM golang:1.8.3  
RUN wget -O /swarm.jar https://repo.jenkins-ci.org/releases/org/jenkins-
ci/plugins/swarm-client/1.22/swarm-client-1.22-jar-with-dependencies.jar  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install -t jessie-backports openjdk-8-jdk  
  
CMD java -jar /swarm.jar -username $JENKINS_USERNAME -password $JENKINS_APIKEY
-labels 'golang swarm'  

