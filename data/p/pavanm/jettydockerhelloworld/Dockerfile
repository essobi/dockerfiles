FROM maven:3.3.3-jdk-7  
RUN mkdir --parents /usr/src/app  
ADD . /usr/src/app  
WORKDIR /usr/src/app  
RUN mvn clean install  
  
EXPOSE 8080  
CMD mvn jetty:run  

