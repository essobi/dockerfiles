FROM anapsix/alpine-java:jdk8  
  
MAINTAINER Vowstar Co., Ltd. <support@vowstar.com>  
  
RUN apk --no-cache add git && \  
cd /opt && \  
wget http://www.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz -O apache-maven-3.3.9-bin.tar.gz && \  
tar xzvf apache-maven-3.3.9-bin.tar.gz && \  
rm -rf apache-maven-3.3.9-bin.tar.gz && \  
export PATH=$PATH:/opt/apache-maven-3.3.9/bin && \  
git clone https://github.com/vowstar/mqttKafkaBridge.git && \  
cd mqttKafkaBridge && \  
mvn compile && \  
mvn assembly:assembly && \  
cp /opt/mqttKafkaBridge/target/mqttKafkaBridge-0.1.0-jar-with-dependencies.jar
/opt/mqttKafkaBridge.jar && \  
cd /opt && \  
rm -rf mqttKafkaBridge && \  
rm -rf apache-maven-3.3.9 && \  
apk --purge del git && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["java", "-jar", "/opt/mqttKafkaBridge.jar"]  

