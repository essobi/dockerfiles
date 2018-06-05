FROM openjdk:jre-alpine  
  
RUN apk --no-cache add bash  
  
COPY target/account-api-*-standalone.jar dockerize docker-cmd.sh /app/  
WORKDIR /app  
CMD ["/app/docker-cmd.sh"]  

