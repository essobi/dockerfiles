FROM google/debian:wheezy  
  
MAINTAINER dharmi@gmail.com  
  
# Install JDK with no add-ons  
RUN apt-get update && \  
apt-get -y -f install --no-install-recommends openjdk-7-jdk && \  
apt-get -y -f install curl  
  
# Install Maven  
ENV MAVEN_VERSION 3.3.1  
RUN curl -sSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
ENV MAVEN_HOME /usr/share/maven  
  
#HTTP port  
EXPOSE 8080  
RUN mkdir -p app  
COPY src app/src  
COPY pom.xml app/pom.xml  
  
WORKDIR app  
  
RUN mvn clean package  
  
# Start Tomcat  
CMD ["/usr/bin/java", "-jar", "target/springswagger-0.1.jar"]  

