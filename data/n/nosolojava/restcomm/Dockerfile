FROM gvagenas/restcomm  
  
# create a new deployment folder  
RUN mkdir /apps  
  
# update jboss standalone config to add previous folder  
WORKDIR /opt/Mobicents-Restcomm-JBoss-AS7/standalone/configuration  
RUN sed '/.*<.*subsystem.*deployment-scanner.*>.*$/a <deployment-scanner
name="docker-external-deployments" path="/apps" scan-interval="5000"/>'
standalone-sip.xml >> tmp.xml \  
&& mv standalone-sip.xml standalone-sip.xml.old \  
&& mv tmp.xml standalone-sip.xml  

