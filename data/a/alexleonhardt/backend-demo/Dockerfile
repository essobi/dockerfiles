FROM maven:3.5-jdk-8 as BUILD  
COPY . /usr/src/backend-demo  
RUN mvn -f /usr/src/backend-demo/pom.xml clean package  
COPY config.yml /usr/src/backend-demo/target  
  
FROM java:8-jre  
COPY \--from=BUILD /usr/src/backend-demo/target/demo-backend-*SNAPSHOT.jar
/usr/src/app/jar-with-dependencies.jar  
COPY \--from=BUILD /usr/src/backend-demo/target/config.yml /usr/src/app/  
  
EXPOSE "8888" "8889"  
CMD ["sh", "-c", "java -jar /usr/src/app/jar-with-dependencies.jar server
/usr/src/app/config.yml"]  

