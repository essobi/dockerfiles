FROM java:8  
RUN apt-get update  
RUN apt-get install -y maven  
  
WORKDIR /  
EXPOSE 5000  
ADD . /opt/  
WORKDIR /opt/  
RUN ["mvn", "clean"]  
RUN mvn package -X -Dmaven.test.skip=true  
RUN mv target/fiwoo_rules-External_Actions-0.0.1-SNAPSHOT.jar
target/fiwoo_rules.jar  
  
CMD java -jar target/fiwoo_rules.jar  
  

