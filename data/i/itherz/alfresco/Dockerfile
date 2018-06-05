FROM itherz/rancher-alfresco  
  
ADD init.py /app/  
  
RUN echo "solr.backup.alfresco.cronExpression=0 0 0 1 1 ? 2200" >>
"/opt/alfresco/tomcat/shared/classes/alfresco-global.properties" && \  
echo "solr.backup.archive.cronExpression=0 0 0 1 1 ? 2200" >>
"/opt/alfresco/tomcat/shared/classes/alfresco-global.properties" && \  
echo "solr.secureComms=none" >> "/opt/alfresco/tomcat/shared/classes/alfresco-
global.properties" && \  
echo "system.content.orphanProtectDays=1" >>
"/opt/alfresco/tomcat/shared/classes/alfresco-global.properties" && \  
sed -i 's/JAVA_OPTS=\"-Xms.*/JAVA_OPTS="-Xms384M -Xmx6G -Duser.language=ru
-Duser.region=RU -Duser.country=RU $JAVA_OPTS\"/ig'
/opt/alfresco/tomcat/bin/setenv.sh  
  

