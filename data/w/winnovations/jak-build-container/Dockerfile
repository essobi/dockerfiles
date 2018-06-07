FROM java:8-jdk-alpine  
MAINTAINER w-innovations <jak@w-innovations.com>  
  
# Set desired Gradle version and expected SHA512 hash. Both of these values
must be updated when bumping the Gradle version.  
ENV GRADLE_VERSION 2.13  
ENV GRADLE_SHA512
3b65f8e37e77ecab1c1e385a2124d4be3f52bd2d33004e11a69856f945119df2d0b8bc94bfb03b1a9379ab92921c2c4943524c1400612e866f1926b81bac8354  
  
# Place Docker in /opt as the installed Gradle is an unbundled package.  
ENV GRADLE_HOME "/opt/gradle-${GRADLE_VERSION}"  
# Update package list and upgrade all available packages.  
# libstdc++ is required by Gradle  
# bash is required for Bitbucket Pipelines  
RUN apk update \  
&& apk upgrade \  
&& apk add libstdc++ \  
&& apk add bash  
  
# Download, verify, and unzip Gradle.  
RUN mkdir /opt \  
&& cd /opt \  
&& wget
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -O
gradle-bin.zip \  
&& echo "$GRADLE_SHA512 gradle-bin.zip" | sha512sum -c - \  
&& unzip "gradle-bin.zip" \  
&& ln -s "$GRADLE_HOME/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip"  
  
# Include gradle in PATH  
ENV PATH $PATH:$GRADLE_HOME/bin  

