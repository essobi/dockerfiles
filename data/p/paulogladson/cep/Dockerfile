FROM fabric8/java-jboss-openjdk8-jdk:1.0.13  
MAINTAINER Paulo Gladson <paulopinheiro777@gmail.com>  
  
ENV JAVA_APP_JAR cep-swarm.jar  
ENV AB_OFF true  
  
WORKDIR /opt/  
  
ADD https://www.demoiselle.org/cep/db.tar.gz /opt/db/  
  
CMD ["tar -zxvf /opt/db/db.tar.gz -C /opt/db/"]  
  
ADD https://www.demoiselle.org/cep/cep-swarm.jar /app/  
  
EXPOSE 8080  

