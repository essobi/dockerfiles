FROM mayureshkrishna/java-8:server-jre-8u121-slim  
LABEL maintainer Mayuresh Krishna <mayureshkrishna@gmail.com>  
  
RUN apk update &&\  
apk --no-cache add openssl &&\  
wget -q https://s3.us-east-2.amazonaws.com/coxcomm/springcloud-eureka/spring-
cloud-netflix-eureka-server-1.4.0.jar &&\  
sh -c 'touch /spring-cloud-netflix-eureka-server-1.4.0.jar'  
  
EXPOSE 8761  
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/spring-
cloud-netflix-eureka-server-1.4.0.jar"]  

