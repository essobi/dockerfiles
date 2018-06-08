FROM ubuntu:14.04  
MAINTAINER Luke Smith  
  
RUN apt-get update  
RUN apt-get install -y apt-transport-https openjdk-7-jdk curl make openssh-
client git tar  
  
RUN echo deb https://apt.dockerproject.org/repo ubuntu-trusty main >
/etc/apt/sources.list.d/docker.list \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& apt-get update \  
&& apt-get install -y docker-engine=1.8.3-0~trusty  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD /opt/init.sh  
  
VOLUME ["/opt/jenkins-workspace"]  
  
# Default swarm settings  
ENV JENKINS_SWARM_EXECUTORS 1  
ENV JENKINS_SWARM_MODE exclusive  
  
ADD http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-
ci/plugins/swarm-client/2.0/swarm-client-2.0-jar-with-dependencies.jar
/opt/jenkins-swarm/swarm-client.jar  
  
COPY set_environment_variables.sh /tmp/set_environment_variables.sh  
COPY init.sh /opt/init.sh  

