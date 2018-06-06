FROM maven:3-jdk-8  
COPY . /usr/src/warcbase  
WORKDIR /usr/src/warcbase  
  
RUN mvn clean package -pl warcbase-core -DskipTests  
  
ADD http://d3kbcqa49mib13.cloudfront.net/spark-1.6.1-bin-hadoop2.6.tgz
/usr/src/spark/spark.tgz  
WORKDIR /usr/src/spark  
RUN tar xzvf spark.tgz  
  
ENTRYPOINT ["/usr/src/spark/spark-1.6.1-bin-hadoop2.6/bin/spark-shell", "--
jars", "/usr/src/warcbase/warcbase-core/target/warcbase-core-0.1.0-SNAPSHOT-
fatjar.jar"]  

