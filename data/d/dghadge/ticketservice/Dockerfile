FROM java:8  
ADD target/ticketingservice-1.0.1-RELEASE.war app.war  
  
RUN sh -c 'touch /app.war'  
  
EXPOSE 8090  
ENV JAVA_OPTS=""  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar /app.war" ]  

