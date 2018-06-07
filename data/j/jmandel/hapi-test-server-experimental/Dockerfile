FROM dockerfile/java:oracle-java8  
MAINTAINER Josh Mandel "Joshua.Mandel@childrens.harvard.edu"  
RUN mkdir /hapi && mkdir /tools  
RUN wget http://central.maven.org/maven2/org/eclipse/jetty/jetty-
runner/9.3.0.M1/jetty-runner-9.3.0.M1.jar -O /tools/jetty-runner.jar  
  
RUN apt-get update  
RUN apt-get install -y maven  
  
EXPOSE 9090  
WORKDIR /hapi  
ADD . /hapi  
RUN mvn install -DskipTests=true  
ENTRYPOINT java \  
-Dfhir.baseurl=http://localhost:9090 \  
-Dfhir.db.location=/tmp/fhirdb.derby \  
-jar /tools/jetty-runner.jar \  
\--port 9090 hapi-fhir-jpaserver-uhnfhirtest/target/hapi-fhir-jpaserver.war  

