FROM tomcat:7.0.69-jre7  
  
# Add JDK  
RUN apt-get update && apt-get install -y openjdk-7-jdk  
  
# Install Maven to build the WAR-File  
RUN wget --no-verbose -O /tmp/apache-maven.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
RUN echo "516923b3955b6035ba6b0a5b031fbd8b /tmp/apache-maven.tar.gz" | md5sum
-c  
RUN tar xzf /tmp/apache-maven.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.3.9 /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven.tar.gz  
ENV MAVEN_HOME /opt/maven  
ENV PATH $MAVEN_HOME/bin:$PATH  
  
WORKDIR /ddd  
  
# Add POM and source  
ADD pom.xml /ddd/pom.xml  
ADD src /ddd/src  
  
# Build the app  
RUN ["mvn", "clean", "package", "-DskipTests" ]  
  
# Deploy WAR-File to tomcat  
RUN cp /ddd/target/dddsample-1.1.0.war /usr/local/tomcat/webapps/ddd-
sample.war  
  
# RUN tomcat  
CMD ["catalina.sh", "run" ]  
  

