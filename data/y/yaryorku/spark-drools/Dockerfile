FROM corba/spark  
MAINTAINER Yar  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# copy the Spark Drools Application  
ADD vScanner_Project/pom.xml /vScanner_Project/pom.xml  
# COPY vScanner_Project/src/main/java/com/sample/SparkDroolsBase.java
/vScanner_Project/src/main/java/com/sample/SparkDroolsBase.java  
# COPY vScanner_Project/src/main/java/com/sample/SecLogTranslator.java
/vScanner_Project/src/main/java/com/sample/SecLogTranslator.java  
# COPY vScanner_Project/src/main/java/com/sample/WSAlert.java
/vScanner_Project/src/main/java/com/sample/WSAlert.java  
ADD vScanner_Project/src/main/resources/META-INF/maven/pom.properties
/vScanner_Project/src/main/resources/META-INF/maven/pom.properties  
ADD vScanner_Project/src/main/resources/META-INF/kmodule.xml
/vScanner_Project/src/main/resources/META-INF/kmodule.xml  
  
ADD vScanner_Project/src/main/resources/rules/aggregate-rules.drl
/vScanner_Project/src/main/resources/rules/aggregate-rules.drl  
ADD vScanner_Project/src/main/resources/rules/seclog-rules.drl
/vScanner_Project/src/main/resources/rules/seclog-rules.drl  
ADD vScanner_Project/src/main/resources/rules/snort-rules.drl
/vScanner_Project/src/main/resources/rules/snort-rules.drl  
  
ADD vScanner_Project/src/main/resources/rules/aggregate-rules.drl
/DroolRules/aggregate-rules.drl  
ADD vScanner_Project/src/main/resources/rules/seclog-rules.drl
/DroolRules/seclog-rules.drl  
ADD vScanner_Project/src/main/resources/rules/snort-rules.drl
/DroolRules/snort-rules.drl  
  
ADD vScanner_Project/target/vScanner.artifact-1.0-SecLog.jar
/vScanner_Project/target/vScanner.artifact-1.0-SecLog.jar  
ADD vScanner_Project/target/vScanner.artifact-1.0-Snort.jar
/vScanner_Project/target/vScanner.artifact-1.0-Snort.jar  
ADD vScanner_Project/target/vScanner.artifact-1.0-Aggregate.jar
/vScanner_Project/target/vScanner.artifact-1.0-Aggregate.jar  
ADD pom.xml /pom.xml  
  
  
# install Maven  
RUN apt-get -y update && \  
apt-get -y install maven && \  
apt-get -y install netcat && \  
mvn dependency:get -Dartifact=org.apache.spark:spark-core_2.10:2.1.0:jar && \  
mvn dependency:get -Dartifact=org.drools:drools-core:6.4.0.Final:jar && \  
mvn dependency:get -Dartifact=org.drools:drools-compiler:6.4.0.Final:jar && \  
mvn dependency:get -Dartifact=org.kie:kie-api:6.4.0.Final:jar && \  
mvn dependency:get -Dartifact=org.kie:kie-internal:6.4.0.Final:jar && \  
mvn dependency:get -Dartifact=com.googlecode.json-simple:json-simple:1.1.1:jar
&& \  
mvn dependency:copy-dependencies
-DoutputDirectory="/vScanner_Project/target/dependency-jars/"
-Dartifact=org.apache.spark:spark-core_2.10:2.1.0:jar && \  
mvn dependency:copy-dependencies
-DoutputDirectory="/vScanner_Project/target/dependency-jars/"
-Dartifact=org.drools:drools-core:6.4.0.Final:jar && \  
mvn dependency:copy-dependencies
-DoutputDirectory="/vScanner_Project/target/dependency-jars/"
-Dartifact=org.drools:drools-compiler:6.4.0.Final:jar && \  
mvn dependency:copy-dependencies
-DoutputDirectory="/vScanner_Project/target/dependency-jars/"
-Dartifact=org.kie:kie-api:6.4.0.Final:jar && \  
mvn dependency:copy-dependencies
-DoutputDirectory="/vScanner_Project/target/dependency-jars/"
-Dartifact=org.kie:kie-internal:6.4.0.Final:jar && \  
mvn dependency:copy-dependencies
-DoutputDirectory="/vScanner_Project/target/dependency-jars/"
-Dartifact=com.googlecode.json-simple:json-simple:1.1.1:jar  
  
### Spark ports  
# 8080: default website  
EXPOSE 8080  
  
  

