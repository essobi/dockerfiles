FROM openjdk:8-alpine  
  
ENV GRADLE_VERSION="4.7"  
RUN apk add --no-cache \  
curl  
  
RUN curl -O --location
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
mkdir /opt && \  
unzip -q gradle-${GRADLE_VERSION}-bin.zip -d /opt && \  
ln -s /opt/gradle-${GRADLE_VERSION} /opt/gradle && \  
rm -f gradle-${GRADLE_VERSION}-bin.zip  
  
ENV PATH $PATH:/opt/gradle/bin  
  
WORKDIR /etc/gradle  
  
ENTRYPOINT ["gradle"]  

