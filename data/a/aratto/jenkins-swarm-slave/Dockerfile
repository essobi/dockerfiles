FROM java:8-jdk  
  
MAINTAINER Andrea Ratto  
  
ENV JENKINS_SWARM_VERSION 1.22  
ENV JENKINS_SLAVE_HOME /var/lib/jenkins_slave  
ENV JENKINS_JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN useradd -c "Jenkins Slave user" -d $JENKINS_SLAVE_HOME -m jenkins_slave  
RUN curl --create-dirs -sSLo \  
/usr/share/jenkins/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar \  
http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-
ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-
client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar && \  
chmod 755 /usr/share/jenkins  
  
COPY jenkins-slave-entrypoint.sh /  
ENTRYPOINT ["/jenkins-slave-entrypoint.sh"]  
  
VOLUME $JENKINS_SLAVE_HOME  

