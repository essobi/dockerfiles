FROM maven:onbuild-alpine  
  
COPY wait-for-it.sh /bin/wait-for-it.sh  
RUN chmod +x /bin/wait-for-it.sh  
  
EXPOSE 6306  
ENTRYPOINT ["java", "-Xms256m", "-Xmx256m", "-XX:+UseG1GC",
"-XX:MaxGCPauseMillis=200", "-jar","target/vostok-airlock-
gate-1.0-SNAPSHOT.jar"]  

