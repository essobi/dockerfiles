# Leadware  
#  
# Jenkins CI Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-jenkins  
# https://jetune@bitbucket.org/leadware/dockerfile-jenkins.git  
# git@bitbucket.org:leadware/dockerfile-jenkins.git  
#  
# Pull base image.  
FROM jenkins/jenkins:lts  
  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# Docker compose version  
ARG DOCKER_COMPOSE_VERSION=1.11.2  
# Docker compose home  
ARG DOCKER_COMPOSE_HOME=/usr/local/bin  
  
# Docker machine version  
ARG DOCKER_MACHINE_VERSION=v0.10.0  
# Docker machine home  
ARG DOCKER_MACHINE_HOME=/usr/local/bin  
  
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
# Root User  
USER root  
  
# Create Maven directories, download and untar maven.  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get install -y apt-transport-https && \  
apt-get install -y ca-certificates && \  
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \  
add-apt-repository -y "deb [arch=amd64]
https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get install -y docker-ce && \  
apt-get install -y ruby && \  
apt-get install -y ivy && \  
apt-get install -y make && \  
apt-get install -y git && \  
curl -L
"https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-$(uname -s)-$(uname -m)" -o $DOCKER_COMPOSE_HOME/docker-compose && \  
chmod +x $DOCKER_COMPOSE_HOME/docker-compose && \  
curl -L
https://github.com/docker/machine/releases/download/$DOCKER_MACHINE_VERSION/docker-
machine-$(uname -s)-$(uname -m) -o $DOCKER_MACHINE_HOME/docker-machine && \  
chmod +x $DOCKER_MACHINE_HOME/docker-machine && \  
mkdir -p $ARG_ANT_HOME_DIR $ARG_MAVEN_HOME_DIR $ARG_MAVEN_LIB_DIR
$ARG_MAVEN_REPO_DIR $ARG_JENKINS_DIR/.m2 && \  
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
usermod -aG docker jenkins  
  
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
# Add Entry point script file  
ADD entrypoint.sh /leadware-entrypoint.sh  
  
# Copy Maven settings to jenkins home  
COPY maven-settings.xml /home/jenkins/.m2/settings.xml  
  
# Give RW wright to entrypoint scripts and .m2 directories  
RUN chmod -R 755 /leadware-entrypoint.sh /home/jenkins/.m2  
  
# Give RWX wright to lib dir and maven home directory  
RUN chmod -R 777 /var/lib/maven /usr/share/ant /usr/share/maven
/usr/share/sonar-scanner  
  
# define volume for maven repository  
VOLUME /var/lib/maven/repository  
  
# define volume for sonar scanner conf  
VOLUME /usr/share/sonar-scanner/conf  
  
# Command  
CMD ["/leadware-entrypoint.sh"]

