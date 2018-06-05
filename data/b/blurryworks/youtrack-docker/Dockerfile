FROM openjdk:9  
MAINTAINER Scott Markwell <scott@blurryworks.com>  
  
RUN mkdir -p /opt/youtrack && \  
curl -o /opt/youtrack/youtrack.jar -L
https://download.jetbrains.com/charisma/youtrack-2018.1.40341.jar  
  
EXPOSE 80/tcp  
VOLUME [ "/data" ]  
CMD java -Xmx1g -XX:MaxMetaspaceSize=250m -Djava.awt.headless=true
-Ddatabase.location=/data -Djetbrains.youtrack.baseUrl=${SERVER_URL} -jar
/opt/youtrack/youtrack.jar 80  
  

