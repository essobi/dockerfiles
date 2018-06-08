FROM tomcat:7  
MAINTAINER "Daniel Betsche" <dbetsche@gmail.com>  
  
RUN mkdir /usr/local/tomcat/db  
COPY SocialFunnelDb.properties /usr/local/tomcat/db/  
COPY SocialFunnelDb.script /usr/local/tomcat/db/  
RUN mkdir /usr/local/tomcat/webapps/tomcat && mv
/usr/local/tomcat/webapps/ROOT/* /usr/local/tomcat/webapps/tomcat/  
RUN rm -R /usr/local/tomcat/webapps/ROOT  
COPY SocialFunnel-1.0.0.war /usr/local/tomcat/webapps/ROOT.war  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["catalina.sh", "run"]  
  
EXPOSE 8080  

