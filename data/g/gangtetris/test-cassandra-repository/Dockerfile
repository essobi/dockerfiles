FROM maven:3  
WORKDIR /usr/src/app  
COPY . .  
RUN mvn package  
  
RUN apt-get update  
RUN apt-get install curl wget netcat -y  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

