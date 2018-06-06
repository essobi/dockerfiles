FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
curl  
  
# Install Docker  
RUN curl -sSL https://get.docker.com/ubuntu/ | sudo sh  
  
# Install Jenkins  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo
apt-key add - \  
&& sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list' \  
&& apt-get update \  
&& apt-get install -y jenkins  
  
# Allow Jenkins to use docker  
RUN gpasswd -a jenkins docker  
  
EXPOSE 8080  
USER jenkins  
VOLUME /var/lib/jenkins  
  
#ENV JAVA /usr/bin/java  
ENV JENKINS_HOME /var/lib/jenkins  
#ENV JAVA_ARGS -Djava.awt.headless=false  
#ENV JENKINS_WAR /usr/share/jenkins/jenkins.war  
#ENV JENKINS_ARGS --webroot=/var/cache/jenkins/war --httpPort=8080
--ajp13Port=-1  
ENV JENKINS_CLIENT /usr/bin/java -jar /var/cache/jenkins/war/WEB-INF/jenkins-
cli.jar -s http://0.0.0.0:8080/  
ENV JENKINS_SERVER /usr/bin/java -Djava.awt.headless=false -jar
/usr/share/jenkins/jenkins.war --webroot=/var/cache/jenkins/war
--httpPort=8080 \--ajp13Port=-1  
# Install Plugins : git docker-build-publish  
RUN /bin/bash -c "$JENKINS_SERVER & \  
until wget -q -O - http://0.0.0.0:8080 > /dev/null; do sleep 1; done && \  
$JENKINS_CLIENT install-plugin http://updates.jenkins-
ci.org/download/plugins/docker-build-publish/0.10/docker-build-publish.hpi &&
\  
$JENKINS_CLIENT install-plugin http://updates.jenkins-
ci.org/download/plugins/git/2.3.5/git.hpi"  
  
CMD [ "/bin/bash", "-c", "$JENKINS_SERVER" ]

