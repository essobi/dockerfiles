# conductor:server - Netflix conductor server  
# First checkout the source and build it  
# stage 0: build the conductor server jar  
FROM azul/zulu-openjdk:8 as builder  
MAINTAINER Netflix OSS <conductor@netflix.com>  
  
RUN apt-get update  
RUN apt-get install -y git  
  
RUN git clone \--branch integer_input_fix https://github.com/PDOK/conductor
/src  
  
WORKDIR /src  
# override the default version logic with an specific version and build it  
RUN ./gradlew -x test build -Prelease.version=$(git describe --tags)  
  
# now create a new container with just the artifacts  
FROM java:8-jre-alpine  
# Make app folders  
RUN mkdir -p /app/config /app/logs /app/libs  
  
# Copy the project directly onto the image, from the previous stage  
# Copy the files for the server into the app folders  
COPY \--from=builder /src/docker/server/bin /app  
COPY \--from=builder /src/docker/server/config /app/config  
  
# override the config  
COPY config.properties /app/config/config.properties  
COPY \--from=builder /src/server/build/libs/conductor-server-*-all.jar
/app/libs  
  
RUN chmod +x /app/startup.sh  
  
EXPOSE 8080  
CMD [ "/app/startup.sh" ]  
ENTRYPOINT [ "/bin/sh"]  

