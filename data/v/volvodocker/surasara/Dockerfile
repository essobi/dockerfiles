FROM openjdk:8-jdk-alpine  
  
RUN mkdir -p /usr/src/myapp  
WORKDIR /usr/src/myapp  
  
COPY hamcrest-core-1.3.jar .  
COPY junit-4.12.jar .  
COPY MinTest.java .  
COPY Min.java .  
  
RUN javac Min.java  
RUN javac -cp .:junit-4.12.jar:hamcrest-core-1.3.jar MinTest.java  
  
CMD java -cp .:junit-4.12.jar:hamcrest-core-1.3.jar org.junit.runner.JUnitCore
MinTest  

