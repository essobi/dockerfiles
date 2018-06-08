FROM ubuntu:14.04  
MAINTAINER Marcello de Sales <marcello.desales@gmail.com>  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
# Utilities  
RUN apt-get update && apt-get -y install software-properties-common unzip  
  
# Install Java.  
RUN apt-get update \  
&& apt-get install -y wget openssl ca-certificates \  
&& cd /tmp \  
&& wget -qO jdk8.tar.gz \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/8u65-b17/jdk-8u65-linux-x64.tar.gz
\  
&& tar xzf jdk8.tar.gz -C /opt \  
&& mv /opt/jdk* /opt/java \  
&& rm /tmp/jdk8.tar.gz \  
&& update-alternatives --install /usr/bin/java java /opt/java/bin/java 100 \  
&& update-alternatives --install /usr/bin/javac javac /opt/java/bin/javac 100  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /opt/java  
  
# Gradle  
ENV GRADLE_VERSION 2.7  
ENV GRADLE_HASH fe801ce2166e6c5b48b3e7ba81277c41  
WORKDIR /usr/lib  
RUN wget
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
RUN echo "${GRADLE_HASH} gradle-${GRADLE_VERSION}-bin.zip" >
gradle-${GRADLE_VERSION}-bin.zip.md5  
RUN md5sum -c gradle-${GRADLE_VERSION}-bin.zip.md5  
RUN unzip "gradle-${GRADLE_VERSION}-bin.zip"  
RUN ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle  
RUN rm "gradle-${GRADLE_VERSION}-bin.zip"  
RUN mkdir -p /usr/src/app  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/src/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Caches  
VOLUME /root/.gradle/caches  
VOLUME /root/.m2/repository  
  
USER $USER  
# Default command is "/usr/bin/gradle -version" on /usr/bin/app dir  
# (ie. Mount project at /usr/bin/app "docker --rm -v /path/to/app:/usr/bin/app
gradle <command>")  
#VOLUME /usr/bin/app  
WORKDIR /usr/bin/app  

