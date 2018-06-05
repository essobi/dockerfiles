FROM maven:3-jdk-8  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN mvn package  
  
CMD java -jar /usr/src/app/target/iris_customer_console-1.0.jar server
/usr/src/app/dw-config.yml  

