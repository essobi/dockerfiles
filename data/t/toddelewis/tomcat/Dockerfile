# Version: 0.0.3  
FROM toddelewis/java:latest  
MAINTAINER Todd Lewis "toddelewis@gmail.com"  
LABEL tomcat-version=8.0.38  
  
RUN yum -y install tar  
RUN curl -O http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.38/bin/apache-
tomcat-8.0.38.tar.gz  
RUN tar xzf apache-tomcat-8.0.38.tar.gz  
RUN yum -y install apr  
CMD /apache-tomcat-8.0.38/bin/catalina.sh run  
EXPOSE 8080  

