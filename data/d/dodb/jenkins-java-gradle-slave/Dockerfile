FROM dodb/jenkins-java-slave  
MAINTAINER David Op de Beeck <davidopdebeeck@hotmail.com>  
  
# Gradle  
ENV GRADLE_VERSION 2.6  
RUN \  
cd /usr/bin && curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
ln -s gradle-${GRADLE_VERSION}/bin/gradle gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
# Enable Gradle daemon  
COPY gradle.properties /home/jenkins/gradle.properties  

