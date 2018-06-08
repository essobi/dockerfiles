FROM tomcat:7.0  
USER root  
RUN apt-get update  
RUN apt-get install --yes vim  
  
#download tomcat-users.xml file and replace existing one  
ADD https://raw.githubusercontent.com/gridfusion-
trainings/cditraining/master/resources/tomcat-users.xml
/usr/local/tomcat/conf/tomcat-users.xml  
  

