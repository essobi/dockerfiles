FROM spantree/ubuntu-oraclejdk8:u31b13  
  
MAINTAINER Cedric Hurst <cedric@spantree.net>  
  
ENV GRADLE_VERSION 2.4  
# Install Gradle  
RUN wget --quiet
https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-all.zip -O
/tmp/gradle-$GRADLE_VERSION-all.zip && \  
cd /tmp && \  
jar -xf gradle-$GRADLE_VERSION-all.zip && \  
mv gradle-$GRADLE_VERSION /opt/gradle && \  
rm -rf /opt/gradle/docs /opt/gradle/samples /opt/gradle/src && \  
chmod a+x /opt/gradle/bin/gradle && \  
rm gradle-$GRADLE_VERSION-all.zip  
  
# Set appropriate Gradle environmental variables  
ENV GRADLE_HOME /opt/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
WORKDIR /  

