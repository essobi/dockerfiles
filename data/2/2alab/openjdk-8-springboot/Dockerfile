FROM openjdk:8-jdk-slim  
  
RUN mkdir /deployments/  
#ENV JAVA_TOOL_OPTIONS  
  
WORKDIR /deployments/  
# ,"-XX:MaxRAMFraction=1" disables  
  
CMD ["java", \  
"-XX:+UnlockExperimentalVMOptions",
"-XX:+UseCGroupMemoryLimitForHeap","-XshowSettings:vm", \  
"-XX:+ExitOnOutOfMemoryError","-XX:+HeapDumpOnOutOfMemoryError",
"-XX:HeapDumpPath=/tmp","-XX:ErrorFile=/tmp/jdk.error", \  
"-XX:MaxHeapFreeRatio=40","-XX:MinHeapFreeRatio=20", \  
"-Djava.security.egd=file:/dev/./urandom", \  
"-Duser.timezone=Europe/Moscow", \  
"-Dspring.profiles.active=production", \  
"-Dserver.port=8080", \  
"-classpath", ".",\  
"org.springframework.boot.loader.JarLauncher"]  

