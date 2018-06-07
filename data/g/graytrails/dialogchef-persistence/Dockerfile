FROM maven:latest AS appserver  
WORKDIR /usr/src/dialogchef  
COPY pom.xml .  
RUN mvn -B -f pom.xml -s /usr/share/maven/ref/settings-docker.xml
dependency:resolve  
COPY . .  
RUN mvn -B -s /usr/share/maven/ref/settings-docker.xml package -DskipTests  
  
EXPOSE 8081  
EXPOSE 8082  
FROM java:8-jdk-alpine  
RUN adduser -Dh /home/dialogchef dialogchef  
WORKDIR /app  
COPY \--from=appserver /usr/src/dialogchef/target/app.jar .  
RUN touch app.jar  
  
ENV DATABASE_HOST database  
ENV DATABASE_PORT 5432  
ENV AUTH_HOST auth_server  
ENV AUTH_PORT 8080  
ENTRYPOINT ["java", "-jar", "/app/app.jar"]  
CMD ["--spring.profiles.active=postgres"]

