FROM glassfish  
  
RUN curl http://repo1.maven.org/maven2/mysql/mysql-connector-
java/5.1.34/mysql-connector-java-5.1.34.jar -o glassfish/lib/mysql-connector-
java-5.1.34.jar  
  
COPY app-server/domain.xml glassfish/domains/domain1/config/domain.xml  
COPY app-server/admin-keyfile glassfish/domains/domain1/config/admin-keyfile  
#  
COPY target/user.war glassfish/domains/domain1/autodeploy/user.war  

