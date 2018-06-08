FROM tomcat:7.0.69-jre7  
  
RUN apt-get update && apt-get install -y openjdk-7-jdk && mkdir -p
/usr/local/tomcat/conf  
  
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
  
WORKDIR /app  
  
ADD pom.xml /app/pom.xml  
ADD src /app/src  
ADD war /app/war  
  
RUN ["mvn","clean","package"]  
  
#RUN rm -fr /usr/local/tomcat/webapps/ROOT  
# Deploy WAR-File to tomcat  
RUN cp /app/target/informationservlet-1.0-SNAPSHOT.war
/usr/local/tomcat/webapps/selfinformation.war  
  
#On local maschine  
#ADD /target/informationservlet-1.0-SNAPSHOT /usr/local/tomcat/webapps/ROOT  
CMD ["catalina.sh", "run" ]  

