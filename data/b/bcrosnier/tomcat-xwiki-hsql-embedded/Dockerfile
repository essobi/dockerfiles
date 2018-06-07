# tomcat 8 and xwiki with default embedded HSQL configuration  
#  
# Uses the default HSQL config -- simply installs the relevant JDBC driver.  
FROM bcrosnier/tomcat-xwiki-base  
  
RUN apt-get update \  
&& apt-get -y install libhsqldb-java \  
&& cp "/usr/share/java/hsqldb.jar" "/usr/share/java/hsqldbutil.jar"
"$XWIKI_ROOT/WEB-INF/lib/"  

