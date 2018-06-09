FROM maven:3-jdk-8-alpine  
MAINTAINER proux UG <info@proux.net>  
  
COPY ./ /app  
  
WORKDIR /app  
  
RUN apk update && apk upgrade \  
&& apk add --no-cache nodejs nodejs-npm git \  
&& npm i --unsafe-perm \  
&& mvn package  
  
EXPOSE 7654  
CMD ["java", "-jar", "target/tikatuka-jar-with-dependencies.jar"]  

