FROM openjdk:8-jdk-alpine  
  
RUN echo "hello"  
  
ADD target/authorization-server-0.0.1-SNAPSHOT.jar authorization-
server-0.0.1-SNAPSHOT.jar  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/authorization-
server-0.0.1-SNAPSHOT.jar"]  
HEALTHCHECK \--interval=1s --timeout=3s \  
CMD curl -f -X GET --header 'Accept: application/json' \--header 'content-
type: application/json' 'http://localhost:8080/users/' || exit 0  
  

