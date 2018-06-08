# Install FROM UBUNTU IMAGE  
FROM ubuntu:16.04  
# Author  
MAINTAINER pictolearn  
  
# RUN COMMAND BASICALLY runs the command in the terminal and creates an image.  
# Install all the updates for UBUNTU  
RUN apt-get update  
  
# Install all the updates for UBUNTU  
RUN apt-get install -y iputils-ping  
  
# Adds the repository where JDK 8 can be obtained for UBUNTU  
#RUN add-apt-repository -y ppa:webupd8team/java  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial
main" >> /etc/apt/sources.list  
  
# INSTALL THE VI EDITOR AND MYSQL-CLIENT  
RUN apt-get install -y vim  
#RUN apt-get install -y mysql-client  
#INSTALL ORACLE JDK 8 BY ACCEPTING YES  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 boolean
true" | debconf-set-selections  
  
#INSTALL ALL the updates again and install MAVEN and JDK 8  
RUN apt-get update && apt-get install -y --allow-unauthenticated oracle-
java8-installer maven  
  
# ADD a directory called spring-boot-jpa-hibernate-docker inside the UBUNTU
IMAGE where you will be moving all of these files under this  
# DIRECTORY to  
ADD . /usr/local/spring-boot-jpa-hibernate-docker  
  
# AFTER YOU HAVE MOVED ALL THE FILES GO AHEAD CD into the directory and run
mvn assembly.  
# Maven assembly will package the project into a JAR FILE which can be
executed  
RUN cd /usr/local/spring-boot-jpa-hibernate-docker && mvn clean package  
  
EXPOSE 8086  
CMD ["java", "-jar", "/usr/local/spring-boot-jpa-hibernate-
docker/target/spring-boot-jpa-hibernate-docker.jar"]  

