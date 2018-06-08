FROM ubuntu:16.10  
MAINTAINER Karl J. Overå  
  
ENV NODE_VERSION 8.4.0  
ENV GRADLE_VERSION 4.1  
RUN apt-get update  
RUN apt-get -y install openjdk-8-jdk wget curl unzip xz-utils python build-
essential ssh git  
  
# Setup certificates in openjdk-8  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# Set path  
ENV PATH ${PATH}:/usr/local/gradle-$GRADLE_VERSION/bin  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs  
  
# Install gradle  
RUN wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
bin.zip && \  
unzip gradle-$GRADLE_VERSION-bin.zip && \  
rm -f gradle-$GRADLE_VERSION-bin.zip  
  
WORKDIR /app  

