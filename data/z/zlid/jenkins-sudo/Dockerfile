FROM java:8-jdk  
  
RUN apt-get update && apt-get install -y wget git curl zip sudo patch bzip2
gawk g++ gcc make libc6-dev patch libreadline6-dev zlib1g-dev libssl-dev
libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev
automake libtool bison pkg-config libffi-dev && rm -rf /var/lib/apt/lists/*  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
# Jenkins is ran with user `jenkins`, uid = 1000  
# If you bind mount a volume from host/volume from a data container,  
# ensure you use same uid  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
RUN chmod +w /etc/sudoers; echo "jenkins ALL=(ALL) NOPASSWD:ALL" >>
/etc/sudoers; chmod -w /etc/sudoers  
# Jenkins home directoy is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_SHA b2d2b6d7f570158ae5eccbad9b98b5e9f040f853  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.14.0/tini-
static -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
ENV JENKINS_VERSION 2.32.2  
ENV JENKINS_SHA f495a08733f69b1845fd2d9b3a46482adb6e6cee  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fL http://mirrors.jenkins-ci.org/war-
stable/$JENKINS_VERSION/jenkins.war -o /usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER jenkins  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# from a derived Dockerfile, can use `RUN plugin.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  

