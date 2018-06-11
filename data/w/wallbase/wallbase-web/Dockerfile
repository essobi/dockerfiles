FROM java:8  
VOLUME /tmp  
ADD wallbase-web-1.0-SNAPSHOT.jar app.jar  
ENV JAVA_OPS -Xmx512M -Xms512M  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPS -jar
-Djava.security.egd=file:/dev/./urandom -Dspring.profiles.active=dev
/app.jar"]  
EXPOSE 8080  

