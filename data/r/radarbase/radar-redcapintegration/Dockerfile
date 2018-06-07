FROM openjdk:8-alpine as builder  
  
RUN mkdir /code  
WORKDIR /code  
  
ENV GRADLE_OPTS -Dorg.gradle.daemon=false  
  
COPY ./gradle/wrapper /code/gradle/wrapper  
COPY ./gradlew /code/  
RUN ./gradlew --version  
  
COPY ./build.gradle ./settings.gradle /code/  
  
RUN ./gradlew downloadApplicationDependencies  
  
COPY ./src/ /code/src  
  
RUN ./gradlew war  
  
FROM tomcat:9-jre8-alpine  
ENV JAVA_OPTS=-Djava.security.egd=file:/dev/urandom  
  
MAINTAINER @yatharthranjan, @blootsvoets  
  
LABEL description="RADAR-CNS Redcap Integration App docker container"  
  
COPY \--from=builder /code/build/libs/*.war /usr/local/tomcat/webapps/  
  
VOLUME /usr/local/tomcat/conf/radar  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

