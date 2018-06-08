FROM node:alpine  
  
LABEL maintainer "NoEnvs"  
LABEL version "1.0.0"  
LABEL description "SonarQube Scanner in NodeJS environment for scanning
typescript and javascript projects"  
  
ENV SONAR_SCANNER_VERSION 3.0.3.778  
ENV JAVA_VERSION 8u131  
ENV JAVA_ALPINE_VERSION 8.131.11-r2  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre  
ENV PATH $PATH:/sonar-
scanner-${SONAR_SCANNER_VERSION}/bin:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ADD "https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_SCANNER_VERSION}.zip" /  
  
RUN set -x \  
&& apk add --no-cache unzip openjdk8-jre="$JAVA_ALPINE_VERSION" \  
&& unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \  
&& rm -f sonar-scanner-cli-*.zip \  
&& mkdir -p /data  
  
VOLUME /data  
WORKDIR /data  

