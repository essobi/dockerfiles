FROM marcelhuberfoo/arch-openjdk8  
MAINTAINER Marcel Huber <marcelhuberfoo@gmail.com>  
  
USER root  
  
RUN pacman -Syy --noconfirm python2 git doxygen graphviz gtk2 openssh wget &&
\  
printf "y\\\ny\\\n" | pacman -Scc  
  
ARG JENKINS_VERSION=2.125  
ARG JENKINS_PKGREL=1  
ENV JENKINS_HOME=/var/lib/jenkins \  
JENKINS_INSTALLDIR=/usr/share/java/jenkins \  
JENKINS_BACKUPDIR=/var/backup/jenkins \  
JENKINS_WEBROOT=/var/cache/jenkins \  
JENKINS_REFDIR=/refdata \  
JENKINS_PORT=8080 \  
JENKINS_SLAVE_AGENT_PORT=50000 \  
JENKINS_UC=https://updates.jenkins.io \  
JENKINS_VERSION=$JENKINS_VERSION \  
JENKINS_PKGREL=$JENKINS_PKGREL \  
JENKINS_OPTS='--webroot=$JENKINS_WEBROOT --httpPort=$JENKINS_PORT' \  
JAVA_OPTS="-Djenkins.security.ArtifactsPermission=true" \  
LC_ALL=en_US.UTF-8  
# `$JENKINS_REFDIR/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p $JENKINS_INSTALLDIR $JENKINS_REFDIR/init.groovy.d
$JENKINS_WEBROOT $JENKINS_BACKUPDIR $JENKINS_HOME  
  
# Indicate jenkins is fully configured for 2.x releases  
RUN echo 2.0 > $JENKINS_REFDIR/jenkins.install.UpgradeWizard.state  
  
COPY init.groovy $JENKINS_REFDIR/init.groovy.d/tcp-slave-agent-port.groovy  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o
$JENKINS_INSTALLDIR/jenkins.war  
  
RUN chown -R $UNAME:$GNAME $JENKINS_HOME $JENKINS_REFDIR $JENKINS_INSTALLDIR
$JENKINS_BACKUPDIR $JENKINS_WEBROOT  
  
# As we use the base containers user to work with, set it's home directory  
# to $JENKINS_HOME to also persist modifications for this user (~/.ssh for
example)  
RUN usermod --home $JENKINS_HOME $UNAME  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
# Jenkins is run with as user `$UNAME`  
# If you bind mount a volume from host/volume from a data container,  
# ensure you use same uid  
VOLUME ["$JENKINS_HOME", "$JENKINS_REFDIR", "$JENKINS_BACKUPDIR"]  
WORKDIR $JENKINS_HOME  
  
# main web interface and slave agents port  
EXPOSE $JENKINS_PORT $JENKINS_SLAVE_AGENT_PORT  
  
# - from a derived Dockerfile, use `RUN plugins.sh plugins.txt` to setup
$JENKINS_REFDIR/plugins from a support bundle  
# - using a temporary container and mounting the refdata volume, use `bash -c
"plugins.sh plugins.txt"` to setup $JENKINS_REFDIR/plugins from a support
bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENV REFCOPY_LOGFILE=$JENKINS_HOME/reference_copy.log  
  
ENTRYPOINT ["/usr/local/bin/jenkins.sh"]  

