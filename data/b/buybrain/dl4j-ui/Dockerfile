FROM java:8  
MAINTAINER Ede Meijer <ede@buybrain.io>  
  
# Install maven  
RUN apt-get update  
RUN apt-get install -y maven  
  
WORKDIR /code  
  
# Prepare by downloading dependencies  
ADD dockerdl4jui/pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify", "-Dmaven.test.skip=true"]  
  
# Add source, compile and package into a fat jar  
ADD dockerdl4jui /code  
RUN ["mvn", "package", "-Dmaven.test.skip=true"]  
  
# Clean up  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Run it  
EXPOSE 9000  
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-cp", "target/docker-
dl4j-ui-0.2.0-bin.jar", "io.buybrain.dockerdl4jui.Server"]  

