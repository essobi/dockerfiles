FROM java:8  
VOLUME /tmp  
ADD target/contactWebApp-0.0.1-SNAPSHOT.jar app.jar  
RUN bash -c 'touch /app.jar'  
EXPOSE 8090  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]  

