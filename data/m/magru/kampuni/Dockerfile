FROM maven:3-jdk-9-slim  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
RUN mvn clean package assembly:single && unzip -d target target/*.zip  
  
FROM openjdk:9-jre-slim  
RUN mkdir /app  
WORKDIR /app  
EXPOSE 8080:8080  
COPY \--from=0 /usr/src/app/target/service .  
#CMD java --module-path /app -m
org.linuxalert.kampuni/org.linuxalert.kampuni.Main  
CMD java -cp "/app/*" \--illegal-access=deny --add-modules java.xml.bind
-Djava.util.logging.config.file=logging.properties org.linuxalert.kampuni.Main  

