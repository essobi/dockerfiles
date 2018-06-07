FROM java:8  
RUN apt-get update  
RUN apt-get install -y maven  
  
WORKDIR /code  
  
ADD start.sh /code/start.sh  
ADD pom.xml /code/pom.xml  
ADD src /code/src  
  
RUN ["mvn", "package"]  
  
EXPOSE 8080  
ENTRYPOINT ["/code/start.sh"]  
  

