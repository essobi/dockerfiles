FROM openjdk:8-jdk as BUILD  
COPY . .  
RUN ./gradlew build  
  
FROM openjdk:8-jre-alpine  
WORKDIR /shihtzu/  
ENV PORT 8080  
EXPOSE 8080  
COPY \--from=BUILD /build/libs/*.jar app.jar  
CMD ["java", "-jar", "app.jar"]  

