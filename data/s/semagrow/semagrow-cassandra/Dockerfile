FROM semagrow/semagrow:test-eval-simple-old  
  
MAINTAINER Yiannis Mouchakis <gmouchakis@iit.demokritos.gr>  
  
  
RUN cd / && \  
git clone https://github.com/semagrow/semagrow.git && \  
cd semagrow && \  
git checkout test-eval-simple-old && \  
mvn clean install && \  
cd / && \  
git clone https://github.com/semagrow/connector-cassandra.git && \  
cd connector-cassandra && \  
mvn clean package && \  
mvn dependency:copy-dependencies && \  
unzip $SEMAGROW_HOME/domains/localhost/webapps/SemaGrow.war -d
$SEMAGROW_HOME/domains/localhost/webapps/SemaGrow/ && \  
cp target/*.jar $SEMAGROW_HOME/domains/localhost/webapps/SemaGrow/WEB-INF/lib/
&& \  
cp target/dependency/*.jar
$SEMAGROW_HOME/domains/localhost/webapps/SemaGrow/WEB-INF/lib/ && \  
cd / && \  
rm -r /semagrow && \  
rm -r /connector-cassandra  
  
CMD cp_resources $SEMAGROW_HOME && catalina.sh run  
  

