FROM openjdk:8u151-jdk-alpine  
  
RUN apk add --no-cache git openssh-client wget curl unzip bash ttf-dejavu
coreutils  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN addgroup -g ${gid} ${group} \  
&& adduser -h /home/jenkins -u ${uid} -G ${group} -s /bin/bash -D ${user}  
  
ENV JENKINS_SWARM_VERSION 3.6  
RUN curl --create-dirs -sSLo /usr/share/jenkins/swarm-client.jar
http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${JENKINS_SWARM_VERSION}/swarm-client-${JENKINS_SWARM_VERSION}.jar && \  
chmod 755 /usr/share/jenkins  
  
RUN mkdir /opt  
  
# RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
COPY swarm/slave.sh /home/jenkins/slave.sh  
RUN chmod +x /home/jenkins/slave.sh  
  
ENTRYPOINT ["/home/jenkins/slave.sh"]  
  
ENV MAVEN_VERSION 3.5.2  
ENV MAVEN_HOME /opt/maven  
ENV SONAR_VERSION 2.4  
ENV GRADLE_VERSION 4.4  
RUN wget --no-verbose -O /tmp/apache-maven-${MAVEN_VERSION}.tar.gz
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz && \  
tar xzf /tmp/apache-maven-${MAVEN_VERSION}.tar.gz -C /opt/ && \  
ln -s /opt/apache-maven-${MAVEN_VERSION} ${MAVEN_HOME} && \  
ln -s ${MAVEN_HOME}/bin/mvn /usr/local/bin && \  
rm -f /tmp/apache-maven-${MAVEN_VERSION}.tar.gz  
  
RUN wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-
dist/${SONAR_VERSION}/sonar-runner-dist-${SONAR_VERSION}.zip && \  
unzip sonar-runner-dist-${SONAR_VERSION}.zip && \  
mv sonar-runner-${SONAR_VERSION} /opt/sonar-runner  
  
RUN mkdir -p /usr/share/gradle/ && \  
curl -fL
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip -o
/usr/share/gradle/gradle-${GRADLE_VERSION}-all.zip && \  
unzip /usr/share/gradle/gradle-${GRADLE_VERSION}-all.zip -d /usr/share/gradle/
&& \  
rm /usr/share/gradle/gradle-${GRADLE_VERSION}-all.zip && \  
ln -s /usr/share/gradle/gradle-${GRADLE_VERSION}/bin/gradle /usr/local/bin  
  
RUN chown jenkins:jenkins -R /home/jenkins  
  
USER jenkins  
WORKDIR /home/jenkins  

