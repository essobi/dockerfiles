FROM openjdk:8u131-jdk-alpine  
  
ENV TZ=America/Vancouver  
  
# Install development packages  
RUN apk add --no-cache --update bash curl git openssh unzip tzdata && \  
rm -rf /var/cache/apk/*  
  
# Install Gradle  
ENV GRADLE_VERSION 3.4.1  
RUN cd /usr/lib && \  
curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip && \  
unzip "gradle-bin.zip" && \  
ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle && \  
rm "gradle-bin.zip"  
  
# Set environmental variables  
ENV GRADLE_HOME=/usr/lib/gradle  
ENV PATH=$PATH:$GRADLE_HOME/bin  

