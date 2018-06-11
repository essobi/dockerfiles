FROM maven:3.5.0-jdk-8-alpine  
EXPOSE 8080  
VOLUME /tmp  
ADD . /usr/src/writers  
RUN cd /usr/src/writers && mvn clean install spring-boot:repackage -DskipTests
\  
&& mv target/writers-0.0.1.jar /app.jar  
RUN rm -rf /usr/src/writers/  
ENV JAVA_OPTS=""  
ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar
/app.jar --spring.profiles.active=docker  

