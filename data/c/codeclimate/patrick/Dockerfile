FROM alpine:3.3  
RUN apk --update add curl jq make  
  
ENV DOCKER_VERSION=1.8.3  
ENV
DOCKER_URL=https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION  
RUN curl -o /bin/docker $DOCKER_URL && chmod +x /bin/docker  
  
COPY ./bin /bin  
ENTRYPOINT ["patrick"]  

