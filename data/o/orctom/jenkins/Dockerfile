FROM orctom/java:8u65  
  
ENV JENKINS_VERSION 2.9  
ENV MAVEN_VERSION 3.3.9  
ENV GRADLE_VERSION 2.13  
ENV JENKINS_HOME /var/lib/jenkins  
ENV MAVEN_HOME /usr/share/maven  
ENV GRADLE_HOME /usr/share/gradle  
  
RUN \  
apk add --update git openssh && rm -rf /var/cache/apk/* \  
&& mkdir -p /usr/share/maven/ \  
&& curl -fL
http://www.us.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz -o /tmp/apache-maven-bin.tar.gz \  
&& tar -xf /tmp/apache-maven-bin.tar.gz -C $MAVEN_HOME \--strip-components=1 \  
&& ln -s $MAVEN_HOME/bin/mvn /usr/bin/mvn \  
&& rm /tmp/apache-maven-bin.tar.gz \  
&& curl -fL
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
/tmp/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip /tmp/gradle-${GRADLE_VERSION}-bin.zip -d /tmp/ \  
&& mv /tmp/gradle-${GRADLE_VERSION} ${GRADLE_HOME} \  
&& ln -s $GRADLE_HOME/bin/gradle /usr/bin/gradle \  
&& mkdir -p /usr/share/jenkins/ \  
&& curl -fL http://mirrors.jenkins-ci.org/war/${JENKINS_VERSION}/jenkins.war
-o /usr/share/jenkins/jenkins.war  
  
# install plugins  
COPY plugins.sh /usr/share/jenkins/plugins.sh  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN chmod +x /usr/share/jenkins/plugins.sh  
RUN \  
mkdir -p $JENKINS_HOME/plugins \  
&& /usr/share/jenkins/plugins.sh /usr/share/jenkins/plugins.txt  
  
# slave  
COPY init.groovy $JENKINS_HOME/init.groovy.d/tcp-slave-agent-port.groovy  
  
# jenkins configuration  
COPY config $JENKINS_HOME/  
COPY email-templates $JENKINS_HOME/email-templates/  
  
# prepare for ssh key generation  
COPY .ssh/ /etc/.ssh/  
  
COPY bootstrap.sh /start-jenkins.sh  
  
# volume  
VOLUME ["$JENKINS_HOME"]  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 52000  
ENTRYPOINT ["/start-jenkins.sh"]  
CMD ["-d"]  

