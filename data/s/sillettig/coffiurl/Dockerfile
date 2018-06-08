FROM ubuntu:14.04  
MAINTAINER Giuseppe Silletti <sillettig@gmail.com>  
  
#Update the system  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-
common  
  
# Install Oracle Java 8  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
sudo /usr/bin/debconf-set-selections &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java8-installer  
  
# Install Redis-Server  
RUN apt-get install -y redis-server  
  
COPY coffiURL/public /var/www/html/  
  
#Install Maven  
RUN apt-get install -y maven  
  
ENV MAVEN_HOME /usr/share/maven  
  
#Compile JAR  
ADD coffiURL/pom.xml /code/pom.xml  
ADD coffiURL/src /code/src  
WORKDIR /code  
  
#Build project with maven  
RUN mvn dependency:resolve  
RUN mvn -DskipTests clean package  
  
#Start application  
RUN /usr/lib/jvm/java-8-oracle/bin/java -jar
code/target/coffiURL-0.0.1-SNAPSHOT.jar init  
  
WORKDIR /  
  
#Exposing ports  
EXPOSE 80 6379  
CMD "/bin/bash"  

