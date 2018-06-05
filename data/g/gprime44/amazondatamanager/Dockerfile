FROM gprime44/amazon_acd_cli  
  
VOLUME /data  
VOLUME /config  
  
ENV JAVA_OPTS ""  
ENV SPRING_CONFIG_LOCATION /config/application.properties  
  
WORKDIR /code  
  
ADD pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
  
ADD src /code/src  
RUN ["mvn", "package"]  
  
CMD ["/bin/sh", "-c", "java $JAVA_OPTS -jar /code/target/app.jar
--spring.config.location=$SPRING_CONFIG_LOCATION"]

