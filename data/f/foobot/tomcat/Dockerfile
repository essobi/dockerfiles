FROM tomcat:8.0-jre8  
  
RUN rm -rf /usr/local/tomcat/conf/ && \  
rm -rf /usr/local/tomcat/webapps/ROOT && \  
rm -rf /usr/local/tomcat/webapps/ROOT.war && \  
rm -rf /usr/local/tomcat/webapps/docs && \  
rm -rf /usr/local/tomcat/webapps/examples && \  
rm -rf /usr/local/tomcat/webapps/host-manager && \  
rm -rf /usr/local/tomcat/webapps/manager && \  
apt-get update -y && \  
apt-get install -y awscli jq && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY root /  
  
RUN chmod +x bin/setenv.sh && \  
chmod +x bin/firstStart.sh && \  
chmod +x bin/s3Download.sh  

