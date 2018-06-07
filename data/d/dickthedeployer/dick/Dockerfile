FROM java:8  
VOLUME /tmp  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
ADD . /usr/src/app  
RUN bash -c './mvnw install -DskipTests && cp /usr/src/app/dick-
web/target/dick-web-1.0-SNAPSHOT.jar /app.jar && rm -rf /usr/src/app
/root/.m2'  
  
EXPOSE 8080  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]  

