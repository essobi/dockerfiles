FROM mesosphere/jenkins-dind:0.3.1  
# Please keep each package list in alphabetical order  
# Required dependencies for the Jenkins agent  
RUN apk --update add \  
bash \  
ca-certificates \  
openjdk8 \  
openssh-client  
  
# Optional convenience functions used by most builds  
RUN apk --update add \  
git \  
jq \  
perl \  
py-pip \  
python \  
python3 \  
unzip  
  
# awscli - because ECR access is nice, if needed  
RUN pip install --upgrade awscli  
  
# Add any SSH known hosts to the environment variable $SSH_KNOWN_HOSTS  
ENV SSH_KNOWN_HOSTS github.com  
RUN ssh-keyscan $SSH_KNOWN_HOSTS | tee /etc/ssh/ssh_known_hosts  
  
# JAVA - directly from:  
# https://github.com/docker-
library/openjdk/blob/54c64cf47d2b705418feb68b811419a223c5a040/8-jdk/alpine/Dockerfile  
ENV LANG C.UTF-8  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
ENV JAVA_VERSION 8u92  
ENV JAVA_ALPINE_VERSION 8.92.14-r1  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# install the Jenkins Swarm Agent  
ENV JENKINS_SWARM_VERSION 2.1  
RUN curl --create-dirs -sSLo /usr/share/jenkins/swarm-
client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar http://maven.jenkins-
ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar && \  
chmod 755 /usr/share/jenkins  
COPY jenkins-slave.sh /usr/local/bin/jenkins-slave.sh  
  
ENTRYPOINT ["/usr/local/bin/jenkins-slave.sh"]  
CMD []  

