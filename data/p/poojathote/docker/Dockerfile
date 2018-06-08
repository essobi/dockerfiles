FROM ubuntu  
  
  
RUN apt-get update  
  
ENV TOMCATVER 7.0.63  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes
openjdk-7-jre-headless wget  
RUN (wget -O /tmp/tomcat7.tar.gz
http://www.us.apache.org/dist/tomcat/tomcat-7/v${TOMCATVER}/bin/apache-
tomcat-${TOMCATVER}.tar.gz && \  
cd /opt && \  
tar zxf /tmp/tomcat7.tar.gz && \  
mv /opt/apache-tomcat* /opt/tomcat && \  
rm /tmp/tomcat7.tar.gz && \  
ls -a)  
  
ADD ./run.sh /usr/local/bin/run  
  
### to deploy a specific war to ROOT, uncomment the following 2 lines and
specify the appropriate .war  
RUN rm -rf /opt/tomcat/webapps/docs /opt/tomcat/webapps/examples
/opt/tomcat/webapps/ROOT  
ADD ALMRS-ubuntu-new.war /opt/tomcat/webapps/ROOT.war  
  
EXPOSE 8080  
CMD ["/bin/sh", "-e", "/usr/local/bin/run"]  

