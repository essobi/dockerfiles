FROM openjdk:jdk-alpine  
MAINTAINER Ray Andrew <raydreww@gmail.com>  
  
# Add curl  
RUN apk add --no-cache curl  
  
# Gradle  
ENV GRADLE_VERSION 4.6  
ENV GRADLE_SHA
98bd5fd2b30e070517e03c51cbb32beee3e2ee1a84003a5a5d748996d4b1b915  
  
WORKDIR /opt  
  
RUN curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip  
  
# Check gradle integrity  
RUN echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c -  
  
# Unzip file  
RUN unzip "gradle-bin.zip"  
  
RUN ln -s "/opt/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle  
  
RUN rm "gradle-bin.zip"  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME "/opt/gradle-${GRADLE_VERSION}"  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
WORKDIR /opt/app  
ENTRYPOINT [ "gradle" ]  
CMD ["-version"]  
  

