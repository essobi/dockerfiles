################################################################################  
#  
# .) Build  
# $ docker-compose build jenkins (executed in cd-stack directory)  
# .) Run  
# $ docker-compose up -d jenkins  
#  
################################################################################  
  
  
FROM jenkins/jenkins:2.60.2  
  
ENV MAVEN_VERSION 3.5.0  
ENV MAVEN_HOME /opt/apache-maven-${MAVEN_VERSION}  
ENV DOCKER_COMPOSE_VERSION 1.15.0  
  
USER root  
RUN mkdir -p /opt/jenkins_config/.docker  
ADD config/curlrc /opt/jenkins_config/.curlrc  
ADD certs/ca.pem /opt/jenkins_config/.docker/ca.pem  
ADD certs/cert.pem /opt/jenkins_config/.docker/cert.pem  
ADD certs/key.pem /opt/jenkins_config/.docker/key.pem  
  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
RUN chown -R jenkins:jenkins /opt  
USER jenkins  
  
RUN mkdir -p /opt/maven_config/.m2  
ADD config/settings.xml /opt/maven_config/.m2/settings.xml  
  
COPY config/hudson.tasks.Maven.xml
/usr/share/jenkins/ref/hudson.tasks.Maven.xml  
COPY config/jenkins.mvn.GlobalMavenConfig.xml
/usr/share/jenkins/ref/jenkins.mvn.GlobalMavenConfig.xml  
COPY config/org.jenkinsci.plugins.dockerbuildstep.DockerBuilder.xml
/usr/share/jenkins/ref/org.jenkinsci.plugins.dockerbuildstep.DockerBuilder.xml  
  
RUN wget -qO-
http://www.eu.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz | tar xvz -C /opt  
  
COPY plugins.txt /plugins.txt  
RUN /usr/local/bin/plugins.sh /plugins.txt  

