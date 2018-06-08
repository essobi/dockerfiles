FROM openjdk:10-jre  
EXPOSE 8080  
COPY /MensaAssistent-0.0.1-SNAPSHOT-shaded.jar /app/MensaAssistent.jar  
ENTRYPOINT ["java", "-jar", "--add-modules", "java.xml.bind",
"/app/MensaAssistent.jar"]  

