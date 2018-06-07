FROM maven:3.5-jdk-8-alpine  
  
MAINTAINER Dennis Stritzke <dennis@stritzke.me>  
  
ADD . /app  
  
RUN mvn clean package -f /app/pom.xml && \  
chown 1000300:1000300 /app/target/moneytracker-0.1-SNAPSHOT.jar  
  
EXPOSE 8080  
  
USER 1000300  
  
CMD ["/usr/bin/java", "-jar", "/app/target/moneytracker-0.1-SNAPSHOT.jar",
"-Xmx128m", "-Djava.security.egd=file:/dev/./urandom"]  

