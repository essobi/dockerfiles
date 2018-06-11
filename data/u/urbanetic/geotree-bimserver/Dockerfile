FROM urbanetic/bimserver  
MAINTAINER Oliver Lade <oliver.lade@unimelb.edu.au>  
  
# TODO(orlade): Replace download with JAR built by Maven from added source
code.  
ADD https://github.com/urbanetic/geotree-bimserver-
plugin/releases/download/0.1.0/geotree-bimserver-plugin-0.1.0.jar
$BIMSERVER_APP/WEB-INF/plugins/geotree-bimserver-plugin.jar  
  
# Start the BIMserver process and send a request to perform the initial admin
setup.  
# Admin username is "admin@bimserver.org", and password is "admin".  
# TODO(orlade): Do this more directly by writing to database.  
# The 30 second sleep is required, since starting Tomcat synchronously doesn't
yield once started.  
RUN catalina.sh start && \  
echo "Waiting 30 secs for BIMserver to initialize..." && \  
sleep 30 && \  
curl -X POST localhost:8080/bimserver/json -d
'{"request":{"interface":"org.bimserver.AdminInterface","method":"setup","parameters":{"siteAddress":"http://localhost:8888/bimserver","smtpServer":"bimserver.org","smtpSender":"admin@bimserver.org","adminName":"Administrator","adminUsername":"admin@bimserver.org","adminPassword":"admin"}}}'  

