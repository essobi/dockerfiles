FROM java:8-jdk  
MAINTAINER Korbinian Riedhammer <korbinian@ieee.org>  
  
# Gradle  
ENV GRADLE_VERSION 3.1  
# https://services.gradle.org/distributions/gradle-3.1-bin.zip  
RUN cd /usr/lib \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip"  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/lib/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Caches  
VOLUME ["/root/.gradle/caches", "/usr/bin/app"]  

