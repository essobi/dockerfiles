FROM nesslinger/docker-alpine-java  
  
MAINTAINER Michael Neßlinger <Michael.Nesslinger@gmx.de>  
  
  
RUN apk upgrade --update && \  
apk add --update git curl openssh-client zip unzip ttf-dejavu supervisor  
  
#You can provide Jenkins version and sha  
ARG JENKINS_VERSION  
ARG JENKINS_SHA  
  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.7.1}  
ENV JENKINS_SHA ${JENKINS_SHA:-12d820574c8f586f7d441986dd53bcfe72b95453}  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ENV JENKINS_UC https://updates.jenkins.io  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
VOLUME /var/jenkins_home  
  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
COPY ./configuration/init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-
slave-agent-port.groovy  
COPY ./configuration/jenkins.sh /usr/local/bin/jenkins.sh  
COPY ./configuration/plugins.sh /usr/local/bin/plugins.sh  
COPY ./configuration/install-plugins.sh /usr/local/bin/install-plugins.sh  
  
RUN chmod a+rx /usr/local/bin/*.sh  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o
/usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
CMD ["/usr/local/bin/jenkins.sh"]

