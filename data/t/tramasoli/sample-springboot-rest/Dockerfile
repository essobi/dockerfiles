FROM tramasoli/jenkins-slave:jdk8  
MAINTAINER Fábio Tramasoli <fabio@tramasoli.com>  
LABEL env=des  
RUN cd /tmp && git clone https://github.com/howtoseries/sample-springboot-
rest.git && \  
cd sample-springboot-rest/gs-rest-service-complete/ && \  
mvn package  
EXPOSE 8080  
CMD /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -jar /tmp/sample-
springboot-rest/gs-rest-service-complete/target/*jar

