FROM ubuntu:16.04  
MAINTAINER rcmova@gmail.com  
  
ENV BUILD_TIMESTAMP 201704051337  
ENV LOCALE en_US.UTF-8  
ADD assets/etc/apt /assets/etc/apt  
  
RUN /bin/bash -c 'ln -fs /assets/etc/apt/sources.list /etc/apt/sources.list'
&& /bin/bash -c 'ln -fs /assets/etc/apt/apt.conf.d/99recommends
/etc/apt/apt.conf.d/99recommends'  
  
# depending images' Dockerfile placeholders  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install the magic wrapper.  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
  
#  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
# A few problems with compiling Java from source:  
# 1. Oracle. Licensing prevents us from redistributing the official JDK.  
# 2. Compiling OpenJDK also requires the JDK to be installed, and it gets  
# really hairy.  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
ENV JAVA_VERSION 8u121  
ENV JAVA_DEBIAN_VERSION 8u121-b13-0ubuntu1.16.04.2  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20160321  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
# verify that "docker-java-home" returns what we expect  
[ "$JAVA_HOME" = "$(docker-java-home)" ]; \  
\  
# update-alternatives so that future installs of other OpenJDK versions don't
change /usr/bin/java  
update-alternatives --get-selections | grep $JAVA_HOME | while read line; do
CMD=$(echo $line | awk '{print $1}'); CMD_PATH=$(echo $line | awk '{print
$NF}'); update-alternatives --set $CMD $CMD_PATH; done;  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# If you're reading this and have any feedback on how this image could be  
# improved, please open an issue or a pull request so we can discuss it!  
RUN apt-get update && apt-get install -y git curl && rm -rf
/var/lib/apt/lists/*  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_VERSION 0.14.0  
ENV TINI_SHA 6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64 -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha256sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
# jenkins version being bundled in this docker image  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.46.2}  
  
# jenkins.war checksum, download will be validated using it  
ARG
JENKINS_SHA=aa7f243a4c84d3d6cfb99a218950b8f7b926af7aa2570b0e1707279d464472c7  
  
# Can be used to customize where jenkins.war get downloaded from  
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war  
  
# could use ADD but this one does not check Last-Modified header neither does
it allow to control checksum  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \  
&& echo "${JENKINS_SHA} /usr/share/jenkins/jenkins.war" | sha256sum -c -  
  
ENV JENKINS_UC https://updates.jenkins.io  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  
  
# install basic utils  
RUN apt-get update -qq && \  
# base depends  
DEBIAN_FRONTEND=noninteractive apt-get install -y locales net-tools iputils-
ping iproute2 sysstat iotop tcpdump tcpick bwm-ng tree strace screen rsync
inotify-tools socat wget curl \  
openssh-server openssh-client build-essential automake make autoconf
libpcre3-dev software-properties-common supervisor sudo git vim emacs python-
minimal fontconfig ssmtp mailutils \  
bash-completion less zfs  
  
RUN locale-gen $LOCALE && update-locale LANG=$LOCALE  
  
# installl docker-compose  
ENV DOCKER_COMPOSE_VERSION="1.12.0"  
RUN curl -L
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
# allow jenkins to talk to docker daemon and to perform privileged actions
with sudo  
RUN adduser jenkins docker && adduser jenkins sudo  
# Fixes forced requiretty on ubuntu-16.04  
RUN sed -i -e '/Defaults\s\\+env_reset/a Defaults\texempt_group=sudo'
/etc/sudoers && \  
sed -i -e 's/%sudo\s*ALL=(ALL:ALL) ALL/%sudo\tALL=(ALL) NOPASSWD:ALL/g'
/etc/sudoers  
  
ADD assets/ /assets  
  
VOLUME ["/var/log/supervisor"]  
ENTRYPOINT ["/assets/bin/entrypoint"]  

