FROM openjdk:9.0.1-11-jre-slim  
  
RUN mkdir /var/app  
  
ARG JAR_FILE  
  
COPY ${JAR_FILE} /var/app/default.jar  
  
WORKDIR /var/app  
  
EXPOSE 8080  
CMD java -jar -Djava.security.egd=file:/dev/./urandom default.jar  

