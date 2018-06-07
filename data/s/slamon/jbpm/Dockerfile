FROM jboss/jbpm-workbench:6.2.0.Final  
  
USER root  
  
# Add sources and config assets  
WORKDIR /workspace  
ADD settings.gradle build.gradle gradlew LICENSE ./  
ADD gradle/ ./gradle/  
ADD src/ ./src/  
ADD docker/ ./docker/  
  
# Build WorkItemHandler and deploy dependencies  
RUN ./gradlew getDepsCompile jar \  
&& cp -nav /workspace/build/libs/* $JBOSS_HOME/standalone/deployments/jbpm-
console.war/WEB-INF/lib/ \  
&& rm -rf /root/.gradle /workspace/.gradle  
  
# Add jBPM Custom Configuration files and inject SLAMon handlers to default
templates  
RUN cp docker/standalone-full-slamon.xml docker/jbpm-users.properties
docker/jbpm-roles.properties $JBOSS_HOME/standalone/configuration/ \  
&& cp docker/WorkDefinitions.wid docker/kie-wb-deployment-descriptor.xml
$JBOSS_HOME/standalone/deployments/jbpm-console.war/WEB-INF/classes/META-INF/  
  
# designer backend needs write access to update assets  
RUN chown jboss:jboss $JBOSS_HOME/standalone/configuration/* \  
&& chown -R jboss:jboss $JBOSS_HOME/standalone/deployments/jbpm-
console.war/org.kie.workbench.KIEWebapp/stencilsets  
  
# Run jBPM  
USER jboss  
WORKDIR $JBOSS_HOME/bin/  
CMD ["./standalone.sh", "-b", "0.0.0.0", "--server-config=standalone-full-
slamon.xml"]  

