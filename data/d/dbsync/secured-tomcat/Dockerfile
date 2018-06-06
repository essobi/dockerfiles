FROM tomcat:8-jre8  
MAINTAINER "Naveen-DBSync <naveen.p@mydbsync.com>"  
ADD tomcat-files/server.xml /usr/local/tomcat/conf/  
  
ADD tomcat-files/catalina.jar /usr/local/tomcat/lib/  
ADD tomcat-files/tomcat-users.xml /usr/local/tomcat/conf/  
ADD tomcat-files/context.xml /usr/local/tomcat/conf/  
  
ADD tomcat-files/web.xml /usr/local/tomcat/conf/  
  
RUN rm -rf /usr/local/tomcat/webapps/* ; \  
rm -rf /usr/local/tomcat/work/Catalina/localhost/* ; \  
rm -rf /usr/local/tomcat/conf/Catalina/localhost/*RUN rm -rf
/usr/local/tomcat/webapps/* ; \  
rm -rf /usr/local/tomcat/work/Catalina/localhost/* ; \  
rm -rf /usr/local/tomcat/conf/Catalina/localhost/*  
  
ADD tomcat-files/error.jsp /usr/local/tomcat/webapps/ROOT/  
ADD tomcat-files/index.jsp /usr/local/tomcat/webapps/ROOT/  
  
RUN chmod -R 400 /usr/local/tomcat/conf  
EXPOSE 8009  
EXPOSE 8080  
EXPOSE 8443  
CMD ["catalina.sh", "run"]  

