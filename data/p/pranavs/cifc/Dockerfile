  
FROM java:8  
VOLUME /tmp  
ADD cifc-0.1.0.jar app.jar  
EXPOSE 8080  
RUN bash -c 'touch /app.jar'  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]  

