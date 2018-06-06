# Build file for charliek/jetty9  
# Base image for jetty apps  
# Images can later be run via:  
# $JAVA_HOME/bin/java -jar $JETTY_JAR /path/to/warfile.war  
  
FROM charliek/openjdk-jre-7  
MAINTAINER charlie.knudsen@gmail.com  
  
ENV JETTY_JAR /usr/local/jetty-runner.jar  
RUN curl http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
runner/9.1.0.v20131115/jetty-runner-9.1.0.v20131115.jar -o $JETTY_JAR

