FROM ubuntu:14.04  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
git \  
iptables \  
libxext-dev libxrender-dev libxtst-dev \  
ssh-askpass \  
unzip \  
wget \  
zip  
  
# Install Docker from Docker Inc. repositories.  
ARG DOCKER_VERSION=1.12.0  
RUN curl -L -O
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz  
RUN tar zxf docker-${DOCKER_VERSION}.tgz -C / \  
&& rm docker-${DOCKER_VERSION}.tgz \  
&& cp /docker/* /usr/local/bin \  
&& rm -rf /docker \  
&& mv /usr/local/bin/docker /usr/local/bin/docker.bin \  
&& printf '#!/bin/bash\nsudo docker.bin "$@"\n' > /usr/local/bin/docker \  
&& chmod +x /usr/local/bin/docker  
  
# Install Docker Compose  
ENV DOCKER_COMPOSE_VERSION 1.8.0  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN mv /usr/local/bin/docker-compose /usr/local/bin/docker-compose.bin \  
&& printf '#!/bin/bash\nsudo docker-compose.bin "$@"\n' >
/usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
# Install Jenkins  
ENV JENKINS_HOME=/var/lib/jenkins JENKINS_UC=https://updates.jenkins-ci.org
HOME="/var/lib/jenkins"  
RUN wget --progress=bar:force -O - https://jenkins-ci.org/debian/jenkins-
ci.org.key | apt-key add - \  
&& sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list' \  
&& apt-get update && apt-get install -y jenkins \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Jenkins plugins from the specified list  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY plugins.txt $JENKINS_HOME/  
RUN chmod +x /usr/local/bin/plugins.sh; sleep 1 \  
&& /usr/local/bin/plugins.sh $JENKINS_HOME/plugins.txt  
  
# Make the jenkins user a sudoer  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# Install jobs & setup ownership & links  
RUN chown -R jenkins:jenkins /var/lib/jenkins  
  
# Become the jenkins user (who thinks sudo is not needed for docker commands)  
RUN adduser jenkins sudo  
USER jenkins  
WORKDIR /var/lib/jenkins  
  
# Expose Jenkins default port  
EXPOSE 8080  
# Start the war  
CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]

