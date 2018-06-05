FROM maven:latest  
RUN mkdir -p /usr/local/src/camel  
WORKDIR /usr/local/src/camel  
ADD . /usr/local/src/camel  
RUN mvn dependency:get -Dartifact=org.apache.maven.plugins:maven-downloader-
plugin:1.0  
RUN mvn dependency:get -Dartifact=org.apache.maven.plugins:maven-resources-
plugin:2.6  
RUN mvn dependency:get -Dartifact=org.apache.camel:camel-maven-plugin:2.16.0  
RUN mvn dependency:get -Dartifact=org.apache.maven.plugins:maven-compiler-
plugin:3.3  
CMD ["mvn","camel:run"]  

