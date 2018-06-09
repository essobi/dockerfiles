FROM java:8  
VOLUME /tmp  
RUN mkdir -p /opt/spring/modules  
RUN mkdir -p /opt/spring/launcher  
# ADD artifacts/modules /opt/spring/modules  
# ADD target/spring-cloud-stream-module-launcher-1.0.0.BUILD-SNAPSHOT-exec.jar
module-launcher.jar  
RUN bash -c 'touch /opt/spring/launcher/spring-cloud-stream-module-
launcher-1.0.0.BUILD-SNAPSHOT-exec.jar'  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/opt/spring/launcher/spring-
cloud-stream-module-launcher-1.0.0.BUILD-SNAPSHOT-exec.jar"]  

