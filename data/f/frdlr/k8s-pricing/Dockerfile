FROM docker:1.12.0-dind  
MAINTAINER Florian Rodler <florian.rodler@comsysto.com>  
  
ENV JENKINS_HOME /home/jenkins  
ENV JENKINS_REMOTNG_VERSION 2.7.1  
ENV JAVA_VERSION 8u111  
ENV JAVA_ALPINE_VERSION 8.111.14-r0  
ENV GRADLE_VERSION 3.5  
ENV GRADLE_HOME /usr/local/gradle  
ENV PATH ${PATH}:${GRADLE_HOME}/bin  
  
ENV DOCKER_HOST tcp://0.0.0.0:2375  
# Install requirements  
RUN apk --update add \  
curl \  
bash \  
git \  
sudo \  
openssh \  
py-pip  
  
# compile and install jdk 8  
# A few problems with compiling Java from source:  
# 1. Oracle. Licensing prevents us from redistributing the official JDK.  
# 2. Compiling OpenJDK also requires the JDK to be installed, and it gets  
# really hairy.  
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
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# Install docker-compose with PIP  
RUN pip install docker-compose  
  
# Install Cloud Foundry CLI  
RUN curl -L
"https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar
-zx \  
&& mv cf /usr/local/bin  
  
# Install Gradle  
WORKDIR /usr/local  
RUN curl -LO
"https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip" &&
\  
unzip gradle-$GRADLE_VERSION-bin.zip && \  
rm -f gradle-$GRADLE_VERSION-bin.zip && \  
ln -s gradle-$GRADLE_VERSION gradle  
# Necessary to avoid error "Failed to load native library 'libnative-
platform.so' for Linux amd64."  
RUN apk update && apk add libstdc++ && rm -rf /var/cache/apk/*  
  
ENV HOME $JENKINS_HOME  
  
# Add jenkins user  
RUN adduser -D -h $JENKINS_HOME -s /bin/sh jenkins jenkins \  
&& chmod a+rwx $JENKINS_HOME  
  
# Allow jenkins user to run docker as root  
RUN echo "jenkins ALL=(ALL) NOPASSWD: /usr/local/bin/docker" >
/etc/sudoers.d/00jenkins \  
&& chmod 440 /etc/sudoers.d/00jenkins  
  
# Install Jenkins Remoting agent  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar http://repo.jenkins-
ci.org/public/org/jenkins-ci/main/remoting/2.52/remoting-2.52.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
USER jenkins  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
USER root  
RUN chmod +x /usr/local/bin/jenkins-slave  
RUN chown root:jenkins /usr/local/bin/docker  
  
USER jenkins  
VOLUME $JENKINS_HOME  
WORKDIR $JENKINS_HOME  
  
ENTRYPOINT ["/usr/local/bin/jenkins-slave"]

