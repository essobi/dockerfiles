FROM openjdk:8-jdk-slim-stretch  
MAINTAINER Willie Loyd Tandingan <n3v3rf411@gmail.com>  
  
ENV HOME /home/jenkins  
  
# 994 below must match with the docker group id in the host system  
RUN groupadd -g 1000 jenkins \  
&& useradd -c "Jenkins user" -d $HOME -u 1000 -g 1000 -m jenkins \  
&& groupadd -g 131 dockerubuntumate \  
&& usermod -aG dockerubuntumate jenkins \  
&& groupadd -g 994 dockerami \  
&& usermod -aG dockerami jenkins  
  
LABEL Description="This is a base image, which provides the Jenkins agent
executable (slave.jar)" Vendor="Jenkins project" Version="3.19"  
  
ARG VERSION=3.19  
ARG AGENT_WORKDIR=/home/jenkins/agent  
  
RUN apt-get -qqy update \  
# Phabricator arcanist  
&& apt-get install -y --no-install-recommends git curl php7.0-cli php7.0-curl
openssh-client \  
&& mkdir -p /usr/local/share/phabricator \  
&& git clone -b master --depth 1 https://github.com/phacility/libphutil.git
/usr/local/share/phabricator/libphutil \  
&& git clone -b master --depth 1 https://github.com/phacility/arcanist.git
/usr/local/share/phabricator/arcanist \  
&& ln -fsn /usr/local/share/phabricator/arcanist/bin/arc /usr/local/bin/arc \  
# Docker  
&& apt-get install -y --no-install-recommends apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common \  
&& echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch
stable" > /etc/apt/sources.list.d/docker.list \  
&& curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add \- \  
&& apt-get -qqy update \  
&& apt-get install -y --no-install-recommends docker-ce aufs-tools \  
# Remoting  
&& curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-
ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar
\  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar \  
&& rm -rf /var/lib/apt/lists/*  
  
  
USER jenkins  
ENV AGENT_WORKDIR=${AGENT_WORKDIR}  
RUN mkdir /home/jenkins/.jenkins && mkdir -p ${AGENT_WORKDIR}  
  
VOLUME /home/jenkins/.jenkins  
VOLUME ${AGENT_WORKDIR}  
WORKDIR /home/jenkins  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
ENTRYPOINT ["jenkins-slave"]

