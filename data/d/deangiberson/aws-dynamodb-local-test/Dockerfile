FROM makuk66/docker-oracle-java7  
#FROM ubuntu:14.04  
WORKDIR /root  
  
RUN apt-get update  
RUN apt-get install -q -y maven  
  
RUN mkdir -p src/main/java/com/deangiberson/TestDynamoDB  
  
ADD Main.java /root/src/main/java/com/deangiberson/TestDynamoDB/Main.java  
ADD pom.xml /root/pom.xml  
  
RUN mvn package  
CMD ["java","-cp","target/TestDynamoDB-1.0-jar-with-
dependencies.jar","com.deangiberson.TestDynamoDB.Main"]  

