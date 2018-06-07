FROM openjdk:8-alpine AS build  
WORKDIR /app  
ADD . /app  
RUN ./mvnw package  
FROM openjdk:8-jre-alpine  
COPY \--from=build /app/target/gs-spring-boot-0.1.0.jar /app.jar  
ENTRYPOINT [ "java", "-jar", "/app.jar", "--management.security.enabled=false"
]  
  

