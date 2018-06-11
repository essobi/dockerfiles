FROM tomcat:7.0.62-jre7  
  
MAINTAINER "Wing Lo <wlo@wasoftware.com>"  
RUN rm -rf ${CATALINA_HOME}/webapps/ROOT  
  
ADD OpenFDA.war ${CATALINA_HOME}/webapps/ROOT.war  
  
CMD ["catalina.sh", "run"]  

