FROM java:8  
RUN apt-get update  
RUN apt-get install -y maven  
  
WORKDIR /  
EXPOSE 7000  
ADD . /data-privacy  
WORKDIR /data-privacy  
RUN ["mvn", "clean"]  
RUN mvn package -X -Dmaven.test.skip=true  
RUN mv target/chino-0.0.1-SNAPSHOT-spring-boot.jar target/data-privacy.jar  
  
CMD java -jar target/data-privacy.jar  

