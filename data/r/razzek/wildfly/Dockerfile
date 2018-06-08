FROM jboss/wildfly:9.0.2.Final  
  
RUN mkdir -p $JBOSS_HOME/modules/com/mysql/main/  
  
ADD module.xml $JBOSS_HOME/modules/com/mysql/main/  
  
RUN curl -sfLS https://repo1.maven.org/maven2/mysql/mysql-connector-
java/6.0.5/mysql-connector-java-6.0.5.jar >
$JBOSS_HOME/modules/com/mysql/main/driver.jar \  
&& echo "9d8df5a1f3273110f2a9ad304961bdd03d696d86
$JBOSS_HOME/modules/com/mysql/main/driver.jar" | sha1sum -c  

