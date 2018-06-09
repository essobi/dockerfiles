FROM centos  
MAINTAINER Noha Hazaa <nh.elsherif@gmail.com>  
  
# Define Variable that will be used  
# Java version , build version and sha for verification  
ENV JAVA_VERSION 8u92  
ENV BUILD_VERSION b14  
ENV JAVA_SHA 8aa13a8be51b8fbb09437abe201fadb01b73e0a1a7d8258a1dc73de007f3b5b3  
  
# Gradle version and sha for verification  
ENV GRADLE_VERSION 2.13  
ENV GRADLE_SHA
0f665ec6a5a67865faf7ba0d825afb19c26705ea0597cec80dd191b0f2cbb664  
  
# Install tools  
RUN yum -y upgrade \  
&& yum -y install wget curl unzip  
  
# Install Java 8  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" -O
/tmp/jdk-8-linux-x64.rpm \  
&& echo "$JAVA_SHA /tmp/jdk-8-linux-x64.rpm" | sha256sum -c - \  
&& yum -y install /tmp/jdk-8-linux-x64.rpm \  
&& alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000 \  
&& alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000 \  
&& alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac
200000  
  
# Java Env. Variable  
ENV JAVA_HOME=/usr/java/latest  
ENV PATH=$PATH:$JAVA_HOME/bin  
# Installation checks  
RUN echo "installed Java version is " && java -version  
  
# Install Gradle  
RUN cd /usr/lib \  
&& echo "Downloading Gradle $GRADLE_VERSION" \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip"  
  
# Gradle Env. Variable  
ENV GRADLE_HOME=/usr/lib/gradle  
ENV PATH=$PATH:$GRADLE_HOME/bin  
  
# Caches  
VOLUME ["/root/.gradle/caches", "/usr/bin/app"]  
# Installation checks  
RUN echo "Installed Gradle version " && gradle -version  

