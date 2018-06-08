FROM tomcat:latest  
RUN mkdir -p /usr/local/tomcat/webapps/opc/WEB-INF/lib  
COPY ./mysql-connector-java-5.1.44-bin.jar /usr/local/tomcat/webapps/opc/WEB-
INF/lib  
COPY ./web.xml /usr/local/tomcat/webapps/opc/WEB-INF  
COPY ./db.jsp /usr/local/tomcat/webapps/opc  
CMD ["catalina.sh", "run"]  

