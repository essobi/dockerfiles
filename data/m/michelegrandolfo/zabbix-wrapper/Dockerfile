FROM jboss/wildfly:9.0.2.Final  
  
MAINTAINER m.grandolfo@reply.it  
  
  
ENV JBOSS_CONF_FILE standalone.xml  
ENV JBOSS_CONF_FILEPATH $JBOSS_HOME/standalone/configuration/$JBOSS_CONF_FILE  
  
COPY /$JBOSS_CONF_FILE /$JBOSS_CONF_FILEPATH  
  
COPY launch.sh /launch.sh  
  
USER root  
RUN yum install -y libaio && yum clean all  
RUN chmod 777 /launch.sh  
USER jboss  
  
EXPOSE 3528 \  
3529 \  
4712 \  
4713 \  
7600 \  
8009 \  
8080 \  
8443 \  
9990 \  
9993 \  
23364 \  
45688 \  
45700 \  
54200 \  
55200 \  
57600  
ENV WAR_NAME MonitoringWrapper  
  
ENTRYPOINT sh /launch.sh  
  
COPY /$WAR_NAME.war $JBOSS_HOME/standalone/deployments/$WAR_NAME.war.zip  
RUN unzip $JBOSS_HOME/standalone/deployments/$WAR_NAME.war.zip -d
$JBOSS_HOME/standalone/deployments/$WAR_NAME.war \  
&& touch $JBOSS_HOME/standalone/deployments/$WAR_NAME.war.dodeploy \  
&& rm $JBOSS_HOME/standalone/deployments/$WAR_NAME.war.zip  
COPY /configurations/ $JBOSS_HOME/standalone/deployments/$WAR_NAME.war/WEB-
INF/classes/  

