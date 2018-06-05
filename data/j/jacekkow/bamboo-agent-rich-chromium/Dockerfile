FROM debian:jessie  
MAINTAINER Jacek Kowalski <jkowalsk@student.agh.edu.pl>  
  
# Maven version to install  
ENV MAVEN_INSTALL_VERSION 3.3.9  
# Gradle version to install  
ENV GRADLE_INSTALL_VERSION 2.9  
RUN echo deb http://httpredir.debian.org/debian jessie-backports main >>
/etc/apt/sources.list  
  
# Update system & install dependencies  
RUN apt-get -y update \  
&& apt-get -y install cvs subversion git mercurial openjdk-7-jdk openjdk-8-jdk
ant unzip wget xvfb \  
&& apt-get -y clean  
  
# Install maven (see https://jira.atlassian.com/browse/BAM-16043)  
RUN cd /tmp \  
&& wget
ftp://mirror.reverse.net/pub/apache/maven/maven-3/${MAVEN_INSTALL_VERSION}/binaries/apache-
maven-${MAVEN_INSTALL_VERSION}-bin.tar.gz \  
&& tar xf apache-maven-${MAVEN_INSTALL_VERSION}-bin.tar.gz -C /opt \  
&& rm -f apache-maven-${MAVEN_INSTALL_VERSION}-bin.tar.gz \  
&& ln -s /opt/apache-maven-${MAVEN_INSTALL_VERSION} /opt/apache-maven  
  
# Install gradle  
RUN cd /tmp \  
&& wget
"https://services.gradle.org/distributions/gradle-${GRADLE_INSTALL_VERSION}-bin.zip"
\  
&& unzip gradle-${GRADLE_INSTALL_VERSION}-bin.zip -d /opt \  
&& rm gradle-${GRADLE_INSTALL_VERSION}-bin.zip \  
&& ln -s /opt/gradle-${GRADLE_INSTALL_VERSION} /opt/gradle  
  
# Install node.js  
RUN apt-get -y install npm  
  
# Install chromium and chromedriver  
RUN apt-get -y install chromedriver  
  
# Link JDKs  
RUN ln -s /usr/lib/jvm/java-1.7.0-openjdk-amd64
/usr/lib/jvm/java-1.7.0-openjdk \  
&& ln -s /usr/lib/jvm/java-1.8.0-openjdk-amd64 /usr/lib/jvm/java-1.8.0-openjdk  
  
# Create user and group for Bamboo  
RUN groupadd -r -g 900 bamboo-agent \  
&& useradd -r -m -u 900 -g 900 bamboo-agent  
  
# Common rules  
COPY bamboo-agent.sh /  
  
USER bamboo-agent  
CMD ["/bamboo-agent.sh"]  

