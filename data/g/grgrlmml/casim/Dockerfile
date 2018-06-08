FROM maven:3.2.5-jdk-8  
WORKDIR /code  
  
ADD pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
  
ADD src /code/src  
RUN ["mvn","test"]  
RUN ["mvn","-DskipTests=true", "assembly:single"]  
  
EXPOSE 9000  
CMD ["java", "-Xmx8G", "-cp", "target/casim-0.1-SNAPSHOT-jar-with-
dependencies.jar","org.cacrowd.casim.hybridsim.run.HybridsimServer"]  

