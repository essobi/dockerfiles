FROM tomcat:7-jre7  
  
MAINTAINER "aBelfadel <abdelhadi.belfadel@gmail.com>"  
RUN mkdir /usr/tmp  
RUN mkdir /usr/tmp/FITMAN_TEST_DATA  
RUN chmod 755 /usr/tmp  
RUN chmod 755 /usr/tmp/FITMAN_TEST_DATA  
  
COPY conf/server.xml /usr/local/tomcat/conf/  
COPY conf/tomcat-users.xml /usr/local/tomcat/conf/  
COPY conf/mysql-connector-java-5.1.31-bin.jar /usr/local/tomcat/lib/mysql-
connector-java-5.1.31-bin.jar  
COPY ME/ /usr/local/tomcat/webapps/  
RUN ls -la /usr/local/tomcat/webapps/*  

