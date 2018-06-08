FROM tomcat:alpine  
  
ADD http://54.209.55.182:8081/artifactory/ext-release-
local/org/sourceforge/pebble/pebble/2.6.6-SNAPSHOT-7/pebble-2.6.6-SNAPSHOT-7.war
/usr/local/tomcat/webapps/pebble.war  
run mkdir /usr/local/tomcat/webapps/pebbleblog  
  
CMD ["catalina.sh", "run"]  

