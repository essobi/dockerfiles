FROM sidereal/jre8  
  
ENV RUNDECK_VER=2.11.3 RUNDECK_HOME=/opt/rundeck
PATH=/opt/rundeck/tools/bin:${PATH} LANG=C.UTF-8  
RUN set -x \  
&& mkdir -p ${RUNDECK_HOME} \  
&& cd ${RUNDECK_HOME} \  
&& curl -fsSLO "http://dl.bintray.com/rundeck/rundeck-maven/rundeck-
launcher-${RUNDECK_VER}.jar" \  
&& mv rundeck-launcher-${RUNDECK_VER}.jar rundeck.jar \  
&& java -jar rundeck.jar --installonly  
  
VOLUME [ "/opt/rundeck/etc", "/opt/rundeck/libext", "/opt/rundeck/projects",
"/opt/rundeck/server/config", "/opt/rundeck/server/data",
"/opt/rundeck/server/logs", "/opt/rundeck/server/work", "/opt/rundeck/var" ]  
  
EXPOSE 4440 4443  
WORKDIR /opt/rundeck  
  
CMD [ "java", "-jar", "rundeck.jar" ]  
  

