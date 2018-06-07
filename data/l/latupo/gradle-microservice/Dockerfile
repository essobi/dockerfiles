# An image that facilitates building microservices with gradle. Note that this  
# image uses layer caching to reduce build times.  
# For production builds, use either `docker build --squash` or external tools
like  
# docker-squash to minimize image file size.  
#  
# How to use this image:  
#  
# Inside a project that contains a gradle wrapper, use this Dockerfile:  
#  
########################### Dockerfile
##########################################  
# FROM latupo/gradle-microservice:<theAppropriateTag>  
#################################################################################  
#  
# If you need additional gradle variables like mavenUser and mavenPassword,  
# simply provide a gradle.properties file in the project directory.  
#################################################################################  
  
FROM openjdk:8u121-jdk-alpine  
  
RUN apk add --no-cache bash curl fontconfig ttf-inconsolata  
  
COPY init.gradle gradle.properties /root/.gradle/  
  
ONBUILD WORKDIR /project  
  
# First, we create a layer with the wrapper, gradle plugins and whatnot  
ONBUILD COPY gradle gradle  
# The globbing syntax will copy only if they are present. properties go into
the project directory to merge with defaults  
ONBUILD COPY *gradle.properties *settings.gradle build.gradle gradlew ./  
  
# Same globbing trick to copy the optionally present home.gradle/ contents to
/root/.gradle/ (build.gradle will be ignored in /root/.gradle)  
ONBUILD COPY *.gradle /root/.gradle/  
  
ONBUILD RUN ./gradlew clean  
  
  
# Finally, the packaged artifact  
ONBUILD COPY src src  
ONBUILD RUN ./gradlew build  
  
ONBUILD RUN mv build/libs/*.jar /usr/local/app.jar  
ONBUILD RUN rm -rf /root/.gradle /project  
  
ONBUILD WORKDIR /usr/local/  
  
# Use cgroup memory limits to automatically set heap sizes (should be
automatically done in JDK9)  
CMD ["java", "-XX:+PrintFlagsFinal", "-XX:+UnlockExperimentalVMOptions",
"-XX:+UseCGroupMemoryLimitForHeap", "-jar", "app.jar"]  
  
EXPOSE 8080  

