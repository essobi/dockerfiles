FROM tomcat:8.0.37-jre8  
MAINTAINER "Naveen-DBSync <naveen.p@mydbsync.com>"  
RUN mkdir -p /usr/local/tomcat/dbsync-repl  
COPY dbsync-repl-tomcat-8.0.30/dbsync-repl /usr/local/tomcat/dbsync-repl  
RUN mkdir -p /usr/local/tomcat/webapps  
ADD dbsync-repl-tomcat-8.0.30/DBSync-License.txt /usr/local/tomcat/  
#ADD dbsync-repl-tomcat-8.0.30/webapps /usr/local/tomcat/webapps  
RUN mkdir -p /usr/local/tomcat/work  
COPY dbsync-repl-tomcat-8.0.30/work /usr/local/tomcat/work  
ADD dbsync-repl-tomcat-8.0.30/dbsync.ico /usr/local/tomcat/  
RUN mkdir -p /usr/local/tomcat/scripts  
COPY dbsync-repl-tomcat-8.0.30/scripts /usr/local/tomcat/scripts  
RUN mkdir -p /usr/local/tomcat/conf/Catalina/localhost  
ADD dbsync-repl-tomcat-8.0.30/conf/Catalina/localhost
/usr/local/tomcat/conf/Catalina/localhost  
RUN mkdir -p /usr/local/tomcat/webapi  
COPY dbsync-repl-tomcat-8.0.30/webapi /usr/local/tomcat/webapi  

