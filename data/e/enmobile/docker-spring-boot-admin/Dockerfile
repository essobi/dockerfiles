FROM openjdk  
VOLUME /tmp  
ADD build/libs/*.jar app.jar  
RUN bash -c 'touch /app.jar'  
EXPOSE 8123  
CMD ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]  

