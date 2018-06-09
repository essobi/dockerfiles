FROM openjdk:8u131-jdk-alpine as build  
  
WORKDIR /app  
ADD . .  
  
RUN ./gradlew build  
  
FROM openjdk:8u131-jre-alpine  
WORKDIR /app  
COPY \--from=build /app/build/libs/config-server.jar config-server.jar  
ENTRYPOINT ["java", "-XX:+UnlockExperimentalVMOptions",
"-XX:+UseCGroupMemoryLimitForHeap", "-XX:MaxRAMFraction=2", "-jar", "config-
server.jar"]  

