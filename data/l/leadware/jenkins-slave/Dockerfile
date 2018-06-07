# Leadware  
#  
# Jenkins CI Slave Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-jenkins-slave  
# https://jetune@bitbucket.org/leadware/dockerfile-jenkins-slave.git  
# git@bitbucket.org:leadware/dockerfile-jenkins-slave.git  
#  
# Pull base image.  
FROM openjdk:8u121-jdk  
  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# Ant Version  
ARG ANT_VERSION=1.10.1  
# Ant home  
ARG ARG_ANT_HOME_DIR="/usr/share/ant"  
# Maven Version  
ARG MAVEN_VERSION=3.3.9  
# Sonar Scanner version  
ARG SONAR_SCANNER_VERSION=3.0.1.733  
# Sonar Scanner system  
ARG SONAR_SCANNER_SYSTEM=linux  
  
# Sonar Scanner home  
ARG SONAR_SCANNER_HOME="/usr/share/sonar-scanner"  
# Maven Home directory  
ARG ARG_MAVEN_HOME_DIR="/usr/share/maven"  
# Maven lib directory  
ARG ARG_MAVEN_LIB_DIR="/var/lib/maven"  
# Maven Repository directory  
ARG ARG_MAVEN_REPO_DIR="$ARG_MAVEN_LIB_DIR/repository"  
# Root Dir  
ARG ARG_JENKINS_DIR="/home/jenkins"  
# Jenkis Work Dir  
ARG ARG_JENKINS_WORK_DIR="/var/jenkins_slave_work"  
# Root User  
USER root  
  
# Create jenkins Group/User  
RUN \  
groupadd -g 800 jenkins && \  
useradd -m -p paOnpkaf2qMac -s /bin/bash -g jenkins -G sudo -c "Jenkins CI
Ubuntu 14.04 Slave Server User" jenkins  
  
# Update/Upgrade apt repository, Install OpenSSH Server, Supervisor  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
#sed -i 's/exit 101/exit 0/' /usr/sbin/policy-rc.d && \  
apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get install -y apt-transport-https && \  
apt-get install -y ca-certificates && \  
apt-get install -y ruby && \  
apt-get install -y ivy && \  
apt-get install -y make && \  
apt-get install -y git && \  
apt-get install -y openssh-server && \  
apt-get install -y supervisor && \  
mkdir -p /var/run/sshd $ARG_ANT_HOME_DIR $ARG_MAVEN_HOME_DIR
$ARG_MAVEN_LIB_DIR $ARG_MAVEN_REPO_DIR $ARG_JENKINS_DIR/.m2
$ARG_JENKINS_WORK_DIR && \  
curl -fsSL http://www-us.apache.org/dist//ant/binaries/apache-
ant-$ANT_VERSION-bin.tar.gz | tar -xzC $ARG_ANT_HOME_DIR \--strip-components=1
&& \  
curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar -xzC $ARG_MAVEN_HOME_DIR \--strip-
components=1 && \  
wget -O sonar-scanner-cli-$SONAR_SCANNER_VERSION-$SONAR_SCANNER_SYSTEM.zip
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-$SONAR_SCANNER_VERSION-$SONAR_SCANNER_SYSTEM.zip && \  
unzip -d /usr/share/ sonar-scanner-
cli-$SONAR_SCANNER_VERSION-$SONAR_SCANNER_SYSTEM.zip && \  
rm sonar-scanner-cli-$SONAR_SCANNER_VERSION-$SONAR_SCANNER_SYSTEM.zip && \  
mv /usr/share/sonar-scanner-$SONAR_SCANNER_VERSION-$SONAR_SCANNER_SYSTEM
$SONAR_SCANNER_HOME && \  
ln -s $ARG_ANT_HOME_DIR/bin/ant /usr/bin/ant && \  
ln -s $ARG_MAVEN_HOME_DIR/bin/mvn /usr/bin/mvn && \  
ln -s $SONAR_SCANNER_HOME/bin/sonar-scanner /usr/bin/sonar-scanner && \  
rm -rf /var/lib/apt/lists/*  
  
# Ant Home  
ENV ANT_HOME $ARG_ANT_HOME_DIR  
  
# Maven Home  
ENV MAVEN_HOME $ARG_MAVEN_HOME_DIR  
  
# Maven Config  
ENV MAVEN_CONFIG $ARG_MAVEN_REPO_DIR  
  
# Sonar Runner Home  
ENV SONAR_RUNNER_HOME $SONAR_SCANNER_HOME  
  
# Sonar Scanner Options  
ENV SONAR_SCANNER_OPTS ""  
# Copy Maven settings to jenkins home  
COPY maven-settings.xml /home/jenkins/.m2/settings.xml  
  
# Add Entry point script file  
ADD entrypoint.sh /jenkins-slave-entrypoint.sh  
  
# Add Start SSHD script file  
ADD start-sshd.sh /start-sshd.sh  
  
# Add SSH supervisor configuration  
ADD supervisord-sshd.conf /etc/supervisor/conf.d/supervisord-sshd.conf  
  
# Give wright to all sh file  
RUN chmod 755 /jenkins-slave-entrypoint.sh  
  
## Expose port 22  
EXPOSE 22  
# Command  
CMD ["/jenkins-slave-entrypoint.sh"]

