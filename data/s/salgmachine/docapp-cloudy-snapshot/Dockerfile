FROM salgmachine/mybase:latest  
VOLUME /tmp  
ADD docparser-0.2.0.jar app.jar  
RUN bash -c 'touch /app.jar'  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

