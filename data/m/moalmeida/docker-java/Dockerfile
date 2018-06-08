FROM moalmeida/docker-base:latest  
MAINTAINER "moalmeida" <moalmeida@koinosystems.com>  
  
RUN mkdir -p /app  
VOLUME ["/app"]  
WORKDIR /app  
  
EXPOSE 8080 8443 8081  
CMD ["mvn", "clean", "install", "package", "exec:java"]  

