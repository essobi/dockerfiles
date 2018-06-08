FROM seeruk/java:openjdk-java8  
MAINTAINER Elliot Wright <hello@elliotdwright.com>  
  
COPY provisioning/docker-entrypoint.sh /opt/jenkins-slave-setup/docker-
entrypoint.sh  
COPY provisioning/start-slave.sh /opt/jenkins-slave-setup/start-slave.sh  
  
ENV GOSU_VERSION 1.10  
ENV LC_ALL en_US.UTF-8  
ENV JAVA_OPTS "-Dfile.encoding=UTF8"  
ENV JENKINS_UID 1000  
ENV JENKINS_GID 1000  
ENV JENKINS_HOME /opt/jenkins-slave  
ENV MASTER_HOST "jenkins.docker"  
ENV MASTER_PORT "8080"  
ENV SLAVE_NAME "jenkins-slave"  
ENV SLAVE_WORKSPACE /opt/jenkins-slave  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
build-essential \  
ca-certificates \  
curl \  
git-core \  
iputils-ping \  
language-pack-en-base \  
wget \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& chmod +x /opt/jenkins-slave-setup/docker-entrypoint.sh \  
&& chmod +x /opt/jenkins-slave-setup/start-slave.sh \  
&& mkdir -p /opt/jenkins-slave-setup/provisioning  
  
WORKDIR /opt/jenkins-slave-setup  
  
ENTRYPOINT ["/opt/jenkins-slave-setup/docker-entrypoint.sh"]  
  
CMD [ "/opt/jenkins-slave-setup/start-slave.sh" ]  

