FROM maven:latest  
  
MAINTAINER Author Name <brindasanth@gmail.com>  
  
CMD ["mkdir", "-p", "/opt/brvith/orchestrator"]  
  
CMD ["mkdir", "-p", "/opt/brvith/blueprints/load"]  
  
COPY ${pwd} /opt/brvith/orchestrator  
  
RUN ["ls", "/opt/brvith/orchestrator"]  
  
RUN ["mvn","-f", "/opt/brvith/orchestrator/pom.xml", "clean", "install"]  
  
CMD ["-jar", "/opt/brvith/orchestrator/application/target/orchestrator-
application*.jar"]  
  
EXPOSE 8080  

