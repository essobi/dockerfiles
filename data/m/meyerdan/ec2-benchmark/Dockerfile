FROM camunda/camunda-platform-distro:tomcat-7.2.0  
# copy configuration  
COPY bpm-platform.xml /camunda/server/apache-tomcat-7.0.50/conf/  
  
# add benchmark plugin  
ADD benchmark-plugin.jar /camunda/server/apache-tomcat-7.0.50/lib/  
# add benchmark process application  
ADD benchmark-processes.war /camunda/server/apache-tomcat-7.0.50/webapps/  

