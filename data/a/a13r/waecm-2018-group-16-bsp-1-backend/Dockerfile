# Stage 0: compile src with gradle  
FROM gradle:4.6-jdk-alpine AS BUILD_IMAGE  
USER root  
ENV BUILD_DIR=/gradle_build  
WORKDIR $BUILD_DIR  
RUN chown -R gradle $BUILD_DIR  
  
USER gradle  
ENV GRADLE_USER_HOME=$BUILD_DIR/.cache  
RUN mkdir -p $GRADLE_USER_HOME  
COPY build.gradle .  
COPY src ./src  
RUN gradle build  
  
# Stage 1: run previously compiled jar  
FROM openjdk:8-jre-alpine  
ENV BUILD_DIR=/gradle_build  
WORKDIR /app/  
COPY \--from=BUILD_IMAGE $BUILD_DIR/build/libs/*.jar ./backend.jar  
EXPOSE 8080  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/backend.jar"]

