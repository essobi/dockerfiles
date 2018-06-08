FROM node:8-alpine as builder  
RUN apk update && apk add openjdk8  
ADD . .  
RUN ./gradlew bootRepackage  
  
FROM ubuntu:xenial  
ENV SERVER_PORT=8080  
ENV DEBUG_PORT=8000  
ENV SERVER_PROTOCOL http  
ENV HEALTHCHECK_CONTEXT management/health  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN apt-key fingerprint 0EBFCD88  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update && apt-get install -y docker-ce openjdk-8-jre-headless  
HEALTHCHECK CMD curl -v --fail
${SERVER_PROTOCOL}://localhost:${SERVER_PORT}/${HEALTHCHECK_CONTEXT} || exit 1  
VOLUME /tmp  
COPY \--from=builder build/libs/*.war /app.war  
ENTRYPOINT ["java","-Xms256m", "-Xmx1024m",
"-Djava.security.egd=file:/dev/./urandom","-jar","/app.war"]  

