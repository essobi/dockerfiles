FROM ruby:latest  
  
MAINTAINER Darryl Bresland <darryl.bresland@seopa.com>  
  
ENV HOME /home/jenkins  
ENV JENKINS_SWARM_VERSION 2.0  
ENV JENKINS_SWARM_JAR_PATH /usr/share/jenkins  
ENV JENKINS_SWARM_JAR $JENKINS_SWARM_JAR_PATH/swarm-
client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar  
ENV JENKINS_LABELS ruby_slave  
ENV JENKINS_MODE exclusive  
ENV JENKINS_DESCRIPTION "Ruby with bundler in a docker container."  
ENV JENKINS_EXECUTORS 1  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
openjdk-7-jre-headless \  
git \  
zip  
  
RUN useradd -d $HOME -m jenkins \  
&& mkdir -p $JENKINS_SWARM_JAR_PATH \  
&& chmod 755 $JENKINS_SWARM_JAR_PATH \  
&& curl -sSLo $JENKINS_SWARM_JAR http://maven.jenkins-
ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar  
  
ADD entrypoint.sh /home/jenkins/entrypoint.sh  
RUN chmod +x /home/jenkins/entrypoint.sh && chown jenkins:jenkins
/home/jenkins/entrypoint.sh  
USER jenkins  
ENTRYPOINT ["/home/jenkins/entrypoint.sh"]

