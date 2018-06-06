#  
FROM ubuntu:16.04  
MAINTAINER Mateusz Juda <mateusz.juda@gmail.com>  
ADD usr/local /usr/local  
  
RUN apt-get update -y && apt-get upgrade -yy && DEBIAN_FRONTEND=noninteractive
apt-get install -yy subversion git zip gawk openjdk-.-jre keychain curl twine
python-setuptools python3-setuptools && /usr/local/src/install_jenkins.sh  
  
  
ADD https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/1.26/swarm-client-1.26-jar-with-dependencies.jar
/var/lib/jenkins/swarm-client-jar-with-dependencies.jar  
  
RUN mkdir /var/lib/jenkins/workspace && touch
/var/lib/jenkins/workspace/.placeholde && chown -R jenkins /var/lib/jenkins  
VOLUME /var/lib/jenkins/workspace  
  
WORKDIR /var/lib/jenkins/  
USER jenkins  
  
# ENTRYPOINT ["/bin/bash"]  
ENTRYPOINT ["java", "-jar", "/var/lib/jenkins/swarm-client-jar-with-
dependencies.jar"]  

