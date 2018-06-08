FROM openjdk:8  
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
  
ADD pom.xml /ddd/pom.xml  
ADD src /ddd/src  
  
RUN ["mvn", "clean", "package", "-DskipTests" ]  
  
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar",
"target/dddsample-2.0-SNAPSHOT.jar"]  
  

