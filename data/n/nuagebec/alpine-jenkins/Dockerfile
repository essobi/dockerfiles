FROM nuagebec/alpine-jdk:7  
MAINTAINER Michael Faille "michael@faille.io"  
# Environment Variables  
ENV JENKINS_VERSION 1.642.3  
ENV JENKINS_HOME /var/lib/jenkins  
ENV JENKINS_SHARE /usr/share/jenkins  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ENV JENKINS_UC https://updates.jenkins-ci.org  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
# 1.2.7.2  
# ENV PLAY_VERSION 1.2.1  
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk  
  
RUN apk --update-cache add \  
gnupg \  
tar \  
ruby \  
git \  
zip \  
curl \  
wget \  
bash \  
fontconfig \  
ttf-dejavu \  
openssh-client \  
python && \  
apk --update-cache \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ add \  
apache-ant && \  
export PATH=$PATH:/usr/share/java/apache-ant/bin  
  
ENV PATH $PATH:/usr/share/java/apache-ant/bin  
  
# Add jenkins user  
RUN addgroup jenkins && \  
adduser -h $JENKINS_HOME -D -s /bin/bash -G jenkins jenkins  
  
# Setup directories and rights so Jenkins user can do things without sudo  
COPY systemconfig.sh /tmp/systemconfig.sh  
RUN bash -c /tmp/systemconfig.sh  
  
# Pull LTS version of Jenkins listed above  
RUN curl -fL http://mirrors.jenkins-ci.org/war-
stable/$JENKINS_VERSION/jenkins.war -o $JENKINS_SHARE/jenkins.war  
  
# Setup plugin update command  
COPY plugins.sh /usr/local/bin/plugins  
  
RUN mkdir ~/.ssh  
  
# Volumes  
VOLUME $JENKINS_HOME  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
## Downgrade user to install the rest  
USER jenkins  
  
# Copy additional files needed from repo into container  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
COPY jenkins.sh /usr/local/bin/jenkins  
  
# Install a plugins using script above  
WORKDIR $JENKINS_HOME  
COPY plugins.txt $JENKINS_SHARE/plugins.txt  
RUN /usr/local/bin/plugins $JENKINS_SHARE/plugins.txt  
  
ENTRYPOINT ["/usr/local/bin/jenkins"]  

