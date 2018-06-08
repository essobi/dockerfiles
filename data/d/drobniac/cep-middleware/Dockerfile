FROM zenika/alpine-maven  
  
VOLUME /tmp  
  
EXPOSE 8090  
COPY . /usr/src/app/  
  
RUN mvn compile  
  
RUN mvn package  
  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","./target/cep-
middleware-0.0.1-SNAPSHOT.jar"]

