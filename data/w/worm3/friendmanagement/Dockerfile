FROM maven:3-jdk-8-alpine  
  
ADD ./ /friendmanagement  
RUN cd /friendmanagement && mvn clean package  
RUN cp /friendmanagement/target/friendmanagement.jar app.jar  
RUN sh -c 'touch /app.jar'  
ENV JAVA_OPTS="-Xmx1024m"  
ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar
/app.jar

