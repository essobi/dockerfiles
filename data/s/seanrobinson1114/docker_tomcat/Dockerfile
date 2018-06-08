#specify the image of the vm from which the container will be built  
FROM tomcat:latest  
  
#specify different users and their privaleges  
ADD tomcat-users.xml /usr/local/tomcat/conf/  
  
#specify settings  
ADD settings.xml /usr/local/tomcat/conf/  
  
#add application file  
ADD sample.war /usr/local/tomcat/webapps/  
  
#add setenv.sh file which specifies JVM configurations  
ADD setenv.sh /usr/local/tomcat/bin/  
  

