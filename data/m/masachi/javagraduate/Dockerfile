FROM maven:3.5-jdk-8  
RUN mkdir /srv/tomcat8  
RUN wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.5.9/bin/apache-
tomcat-8.5.9.tar.gz  
RUN tar xf apache-tomcat-8.5.9.tar.gz -C /srv/tomcat8  
ENV CATALINA_HOME /srv/tomcat8/apache-tomcat-8.5.9  
EXPOSE 8080  
RUN mkdir java-graduate  
ADD . /java-graduate  
RUN cd /java-graduate  
WORKDIR /java-graduate  
RUN mvn compile  
RUN mvn package  
RUN cp target/graduate.war /srv/tomcat8/apache-tomcat-8.5.9/webapps/  
CMD ["/srv/tomcat8/apache-tomcat-8.5.9/bin/catalina.sh", "run"]  

