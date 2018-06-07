FROM tomcat:7-jre7  
  
RUN rm -rf /usr/local/tomcat/webapps/ROOT \  
/usr/local/tomcat/webapps/docs \  
/usr/local/tomcat/webapps/examples \  
/usr/local/tomcat/webapps/host-manager \  
/usr/local/tomcat/webapps/manager  
COPY files/vocbench-2.4.4.war /usr/local/tomcat/webapps/ROOT/ROOT.war  
RUN cd /usr/local/tomcat/webapps/ROOT && unzip
/usr/local/tomcat/webapps/ROOT/ROOT.war  
RUN rm /usr/local/tomcat/webapps/ROOT/ROOT.war  
  
VOLUME ["/usr/local/tomcat/logs"]  

