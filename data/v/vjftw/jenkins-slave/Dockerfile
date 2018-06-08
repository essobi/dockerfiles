FROM vjftw/ubuntu  
MAINTAINER VJ Patel <vj@vjpatel.me>  
  
# install git, jdk, curl  
RUN apt-get install -y wget  
RUN apt-add-repository ppa:brightbox/ruby-ng  
RUN echo 'deb http://apt.dockerproject.org/repo ubuntu-trusty main' >
/etc/apt/sources.list.d/docker.list  
RUN apt-get update && apt-get install -y --force-yes git ruby2.2 openjdk-7-jdk
docker-engine  
  
# install swarm-slave  
ENV SWARM_HOME /app  
ENV SWARM_VERSION 2.0  
ENV SWARM_WORKDIR=/opt/jenkins  
RUN mkdir -p $SWARM_WORKDIR  
  
RUN wget --no-check-certificate --directory-prefix=${SWARM_HOME} \  
http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-
ci/plugins/swarm-client/${SWARM_VERSION}/swarm-client-${SWARM_VERSION}-jar-
with-dependencies.jar && \  
mv ${SWARM_HOME}/swarm-client-${SWARM_VERSION}-jar-with-dependencies.jar
${SWARM_HOME}/swarm-client-jar-with-dependencies.jar && \  
chown -R app:app ${SWARM_HOME} && \  
chmod +x ${SWARM_HOME}/swarm-client-jar-with-dependencies.jar  
  
RUN apt-get clean  
  
RUN gem install rake docker-api  
  
# docker entrypoint env variables  
ENV SWARM_VM_PARAMETERS=  
ENV SWARM_MASTER_URL=  
ENV SWARM_VM_PARAMETERS=  
ENV SWARM_JENKINS_USER=  
ENV SWARM_JENKINS_PASSWORD=  
ENV SWARM_CLIENT_EXECUTORS=  
ENV SWARM_CLIENT_LABELS=  
  
COPY jenkins.sh /etc/services.d/jenkins/run  
RUN chmod 755 /etc/services.d/jenkins/run  
  
VOLUME ["/opt/jenkins"]  

