FROM debian:wheezy  
MAINTAINER Lee Faris "lee@talio.co"  
RUN apt-get update -y  
RUN apt-get install curl -y  
  
# Install java 7  
RUN apt-get install openjdk-7-jre-headless -y  
  
RUN curl -o elasticmq-server-0.8.5.jar https://s3-eu-
west-1.amazonaws.com/softwaremill-public/elasticmq-server-0.8.5.jar  
  
CMD ["java", "-jar","elasticmq-server-0.8.5.jar"]  
  
EXPOSE 9324  

