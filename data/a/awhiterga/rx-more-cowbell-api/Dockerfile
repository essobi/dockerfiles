FROM maven:3-jdk-8  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app  
  
RUN mvn clean install  
RUN ln -sfn target/$(ls target | grep rx-more-cow-bell-api-* | grep -v
original) rx-more-cow-bell-api.jar  
  
CMD ["java","-jar","rx-more-cow-bell-api.jar"]

