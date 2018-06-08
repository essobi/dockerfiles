#  
# Gitlab CI - Gradle & Ktlint  
# Oliver Spryn  
#  
# Versions:  
# - Gradle: 3.3  
# - Ktlint: 0.12.1  
#  
# https://hub.docker.com/r/oliverspryn/gitlab-ci-gradle-and-ktlint  
# https://github.com/oliverspryn/gitlab-ci-gradle-and-ktlint  
#  
FROM openjdk:alpine  
LABEL maintainer="Oliver Spryn"  
  
RUN apk update  
RUN apk add bash unzip wget  
  
RUN mkdir -p /build/gradle  
RUN wget -O /build/gradle.zip
https://services.gradle.org/distributions/gradle-3.3-bin.zip  
RUN unzip -d /build/gradle /build/gradle.zip  
RUN rm /build/gradle.zip  
RUN mv /build/gradle/gradle-3.3/* /build/gradle  
RUN rm -rf /build/gradle/gradle-3.3  
  
RUN wget -O /build/ktlint
https://github.com/shyiko/ktlint/releases/download/0.12.1/ktlint  
RUN chmod +x /build/ktlint  
  
ENV PATH "$PATH:/build"  
ENV PATH "$PATH:/build/gradle/bin"

