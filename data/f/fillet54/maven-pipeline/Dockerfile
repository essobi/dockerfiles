FROM maven:3.3.9  
  
COPY pom.xml /tmp/pom.xml  
RUN mvn -B -f /tmp/pom.xml -s /usr/share/maven/ref/settings-docker.xml
dependency:resolve dependency:resolve-plugins verify clean  
  

