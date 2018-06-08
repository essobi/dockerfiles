FROM java:8  
VOLUME /tmp  
#ADD sleuth-eureka-server-0.0.11-SNAPSHOT.jar app.jar  
RUN bash -c 'touch /app.jar'  
EXPOSE 8761  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]  

