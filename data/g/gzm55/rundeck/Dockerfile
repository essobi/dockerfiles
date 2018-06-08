FROM jeanblanchard/java:jdk-8  
# Download  
ADD http://dl.bintray.com/rundeck/rundeck-maven/rundeck-launcher-2.6.11.jar
/opt/rundeck/  
COPY content /  
  
VOLUME ["/opt/rundeck/etc", \  
"/opt/rundeck/var", \  
"/opt/rundeck/projects", \  
"/opt/rundeck/server/config", \  
"/opt/rundeck/server/data", \  
"/opt/rundeck/server/logs"]  
  
EXPOSE 4440 4443  
ENTRYPOINT ["/opt/rundeck/entrypoint.sh"]  

