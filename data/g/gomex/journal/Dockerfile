FROM maven:3-jdk-8-alpine  
WORKDIR /code  
COPY ./Code /code  
RUN mvn clean package -Dmaven.test.skip=true  
EXPOSE 8000  
CMD ["/usr/bin/java", "-jar", "/code/target/journals-1.0.jar", "--
server.port=8000"]  

