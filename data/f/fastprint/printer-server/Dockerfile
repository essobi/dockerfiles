FROM maven:3.5.0-jdk-8  
COPY . /usr/src/printer-server  
WORKDIR /usr/src/printer-server  
RUN mvn dependency:resolve  
RUN mvn clean install  
  
# Expose  
EXPOSE 50055 8080  
ENTRYPOINT [ "java", "-Djava.security.egd=file:/dev/./urandom","-jar",
"/usr/src/printer-server/target/printer-0.0.1-SNAPSHOT.jar"]  

