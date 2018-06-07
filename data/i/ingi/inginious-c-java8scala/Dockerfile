# DOCKER-VERSION 1.1.0  
#inherit from the base container, which have all the needed script to launch
tasks  
FROM ingi/inginious-c-base  
LABEL org.inginious.grading.name="java8scala"  
  
RUN yum -y install wget java-1.8.0-openjdk-devel && \  
wget -P /usr/share/scala/lib -O scalacheck.jar
https://www.scalacheck.org/files/scalacheck_2.12-1.13.4.jar && \  
wget -P /usr/share
http://search.maven.org/remotecontent?filepath=junit/junit/4.12/junit-4.12.jar
&& \  
wget -P /usr/share
http://search.maven.org/remotecontent?filepath=org/hamcrest/hamcrest-
core/1.3/hamcrest-core-1.3.jar && \  
yum -y remove wget && \  
rpm -ivh https://downloads.lightbend.com/scala/2.12.2/scala-2.12.2.rpm && \  
yum clean all  

