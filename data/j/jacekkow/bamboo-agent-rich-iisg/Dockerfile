FROM centos:7  
MAINTAINER Jacek Kowalski <jkowalsk@student.agh.edu.pl>  
  
# Maven version to install  
ENV MAVEN_INSTALL_VERSION 3.3.9  
# Gradle version to install  
ENV GRADLE_INSTALL_VERSION 2.9  
# JRuby version to install  
ENV JRUBY_INSTALL_VERSION 9.0.4.0  
# PhantomJS version to install  
ENV PHANTOMJS_INSTALL_VERSION 1.9.8  
# Update system & install dependencies  
RUN yum -y update \  
&& yum -y install cvs subversion git mercurial java-1.7.0-openjdk-devel
java-1.8.0-openjdk-devel ant bzip2 unzip wget which xorg-x11-server-Xvfb \  
&& yum -y clean all  
  
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
  
# Install JRuby  
RUN cd /tmp \  
&& wget
"https://s3.amazonaws.com/jruby.org/downloads/${JRUBY_INSTALL_VERSION}/jruby-
bin-${JRUBY_INSTALL_VERSION}.tar.gz" \  
&& tar xf jruby-bin-${JRUBY_INSTALL_VERSION}.tar.gz -C /opt \  
&& rm -f jruby-bin-${JRUBY_INSTALL_VERSION}.tar.gz \  
&& ln -s /opt/jruby-${JRUBY_INSTALL_VERSION} /opt/jruby  
  
# Install Oracle JDK  
RUN wget --no-check-certificate --no-cookies \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/8u65-b17/jdk-8u65-linux-x64.rpm \  
&& yum -y localinstall jdk-8u65-linux-x64.rpm \  
&& rm -f jdk-8u65-linux-x64.rpm  
  
# Install node.js  
RUN yum -y install epel-release \  
&& yum -y install nodejs  
  
# Install PhantomJS  
RUN cd /tmp \  
&& wget
"https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_INSTALL_VERSION}-linux-x86_64.tar.bz2"
\  
&& tar xf phantomjs-${PHANTOMJS_INSTALL_VERSION}-linux-x86_64.tar.bz2 -C /opt
\  
&& rm -f phantomjs-${PHANTOMJS_INSTALL_VERSION}-linux-x86_64.tar.bz2 \  
&& ln -s /opt/phantomjs-${PHANTOMJS_INSTALL_VERSION}-linux-x86_64
/opt/phantomjs  
  
# Create user and group for Bamboo  
RUN groupadd -r -g 900 bamboo-agent \  
&& useradd -r -m -u 900 -g 900 bamboo-agent  
  
COPY bamboo-agent.sh /  
  
USER bamboo-agent  
CMD ["/bamboo-agent.sh"]  

