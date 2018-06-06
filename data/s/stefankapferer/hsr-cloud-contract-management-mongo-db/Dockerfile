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
  
WORKDIR /contract-management  
  
# Add POM and source  
ADD pom.xml /contract-management/pom.xml  
ADD src /contract-management/src  
ADD res /contract-management/res  
ADD WebContent /contract-management/WebContent  
  
# Build the app  
RUN ["mvn", "clean", "package" ]  
  
# Deploy WAR-File to tomcat  
RUN cp /contract-management/target/MongoDB_Servlet-0.0.1-SNAPSHOT.war
/usr/local/tomcat/webapps/ContractManagement.war  
  
# RUN tomcat  
CMD ["catalina.sh", "run" ]  
  

