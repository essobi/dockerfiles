from tomcat:7-alpine  
COPY setenv.sh /usr/local/tomcat/bin/  
COPY tomcat-users.xml /usr/local/tomcat/conf/  
RUN rm -rf /usr/local/tomcat/webapps/ROOT/* && rm -rf
/usr/local/tomcat/webapps/docs /usr/local/tomcat/webapps/examples  
  
EXPOSE 8080  
VOLUME ["/usr/local/tomcat/webapps/"]  
CMD ["catalina.sh", "run"]

