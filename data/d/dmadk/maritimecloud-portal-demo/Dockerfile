FROM jboss/wildfly:9.0.1.Final  
  
RUN curl -o /opt/jboss/wildfly/standalone/deployments/mcportal.zip
https://dma.ci.cloudbees.com/job/MaritimeCloudPortalDemo/lastSuccessfulBuild/net.e2.bw.servicereg\$bw-
servicereg-web/artifact/net.e2.bw.servicereg/bw-servicereg-
web/**/*.war/*zip*/mcportal.zip  
  
RUN unzip -j -C /opt/jboss/wildfly/standalone/deployments/mcportal.zip *.war
-d /opt/jboss/wildfly/standalone/deployments/  
  
RUN rm /opt/jboss/wildfly/standalone/deployments/mcportal.zip  
  
RUN ls -la /opt/jboss/wildfly/standalone/deployments  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]  

