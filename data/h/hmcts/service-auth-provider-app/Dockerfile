#### Create Jar  
FROM gradle:jdk8 as builder  
  
COPY . /home/gradle/app  
USER root  
RUN chown -R gradle:gradle /home/gradle/app  
  
USER gradle  
WORKDIR /home/gradle/app  
  
RUN mkdir -p api/src/main/resources/META-INF \  
&& echo "build.version=$(gradle -q printVersion)" >
api/src/main/resources/META-INF/build-info.properties \  
&& echo "build.number=${BUILD_NUMBER:=docker}" >> api/src/main/resources/META-
INF/build-info.properties \  
&& echo "build.commit=$(git rev-parse HEAD)" >> api/src/main/resources/META-
INF/build-info.properties \  
&& echo "build.date=$(date)" >> api/src/main/resources/META-INF/build-
info.properties  
  
RUN gradle installDist  
  
#### Actual DockerFile  
FROM openjdk:8-jre  
  
MAINTAINER "HMCTS <https://github.com/hmcts>"  
LABEL maintainer = "HMCTS <https://github.com/hmcts>"  
  
WORKDIR /opt/app  
COPY \--from=builder /home/gradle/app/api/build/install/service-auth-provider-
api .  
  
HEALTHCHECK \--interval=10s --timeout=10s --retries=10 CMD http_proxy="" curl
--silent --fail http://localhost:8489/health  
  
EXPOSE 8489  
ENTRYPOINT [ "/opt/app/bin/service-auth-provider-api" ]  

