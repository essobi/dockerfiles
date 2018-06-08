#FROM tomcat:8.0  
#RUN apt-get update && \  
# apt-get -y upgrade && \  
# apt-get install -y vim maven  
#FROM cckm/tomcat:basic  
FROM naboson/cckm_tomcat:latest  
  
# Remove garbage  
RUN rm -rf /opt/tomcat/webapps/examples  
RUN rm -rf /opt/tomcat/webapps/docs  
RUN rm -rf /opt/tomcat/webapps/ROOT  
  
COPY . /usr/src  
WORKDIR /usr/src  
RUN mvn package  
RUN cp target/cckm_web.war /opt/tomcat/webapps/ROOT.war  
  
EXPOSE 8080  
EXPOSE 8009  
CMD ["/opt/tomcat/bin/catalina.sh", "run"]  
  

