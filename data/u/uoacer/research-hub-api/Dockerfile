FROM java:8  
MAINTAINER James Diprose "j.diprose@auckland.ac.nz"  
# Download maven  
ENV MAVEN_VERSION 3.5.0  
ENV MAVEN_CHECKSUM 35c39251d2af99b6624d40d801f6ff02  
RUN wget --no-verbose -O /apache-maven.tar.gz http://www-
us.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz  
  
# Verify checksum  
RUN echo "$MAVEN_CHECKSUM /apache-maven.tar.gz" | md5sum -c  
  
# Install maven  
RUN tar xzf /apache-maven.tar.gz -C /opt/ && mv /opt/apache-
maven-$MAVEN_VERSION /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
ENV MAVEN_HOME /opt/maven  
RUN rm -f /apache-maven.tar.gz  
  
# Copies all files and maintains directory structure  
COPY / /research-hub-api/  
  
# Build research hub api jar with Maven  
WORKDIR /research-hub-api/  
RUN mvn package  
RUN mv target/app.jar /app.jar  
  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]  
  
#,"--spring.config.location=file:/application.properties"]

