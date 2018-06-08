FROM openjdk:8-jre-alpine  
  
#Set the working directory to /app  
WORKDIR /app  
  
#Copy the current directory contents into the container at /app  
ADD /target/tpRevisionXMLJPA-1.0-SNAPSHOT-withdependencies.jar /app  
  
# preserve Java 8 from the maven install.  
#RUN mv /etc/alternatives/java /etc/alternatives/java8  
#RUN apt-get update -y && apt-get install maven -y  
# Restore Java 8  
#RUN mv -f /etc/alternatives/java8 /etc/alternatives/java  
#RUN ls -l /usr/bin/java && java -version  
# Run this command when the containers launches  
CMD ["java", "-jar", "/app/tpRevisionXMLJPA-1.0-SNAPSHOT-
withdependencies.jar"]  

