FROM java:8  
MAINTAINER Phillip Shipley <phillip.shipley@gmail.com>  
  
ENV REFRESHED_AT 2015-12-22  
RUN wget
http://mirror.cogentco.com/pub/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
RUN tar -zxf apache-maven-3.3.9-bin.tar.gz  
  
ENV PATH $PATH:/apache-maven-3.3.9/bin  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
CMD ["mvn","--version"]  

