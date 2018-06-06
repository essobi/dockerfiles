FROM tomcat:7-jre8  
  
MAINTAINER Suparit Krityakien <suparit@wongnai.com>  
  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
COPY war/cyclop-2.0.1.war /usr/local/tomcat/webapps/ROOT.war  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

